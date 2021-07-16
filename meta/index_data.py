import json
import sys
from typing import Union
from meta import *
from constants import *

sys.path.append('/...')


class UserDataIndex:

    def __init__(self, meta_file, index_dir):
        """
        :param meta_file: meta file location of the user
        """
        self.meta_file = meta_file
        self.index_dir = index_dir

    def __level_exists(self, level) -> int:
        """
        Checks if a particular level of indexing exists or not.
        :param level: level
        :return: 1 if the level exists, 0 otherwise
        """
        with open(self.meta_file) as meta_file:
            meta_data = json.load(meta_file)
        highest_level = int(meta_data.get('number_of_levels', 0))
        if level > highest_level:
            return 0
        return 1

    def __get_meta(self) -> dict:
        """
        :return: Meta data as a dictionary
        """
        with open(self.meta_file) as meta_file:
            meta_data = json.load(meta_file)
        return meta_data

    def __write_meta(self, meta_data) -> None:
        """
        Writes data to the meta file
        :param meta_data: Data to be written.
        :return: None
        """
        with open(self.meta_file, 'w') as meta_file:
            json.dump(meta_data, meta_file)

    def get_free_block_size(self, level) -> int:
        """
        :param level: Index level number
        :return: number of records that could be inserted to the level without
        causing an overflow. -1 if level doesn't exists
        """
        lvl = str(level)
        if not self.__level_exists(level):
            return -1

        meta_data = self.__get_meta()
        return BLOCK_SIZE - int(meta_data[lvl]['number_of_entries'])

    def decrement_free_block_size(self, level) -> int:
        """
        This method increases number of records at the given level.
        :param level: level at which new record is inserted.
        :return: 0 on success, -1 on error
        """
        lvl = str(level)
        if not self.__level_exists(level):
            return -1
        meta_data = self.__get_meta()
        meta_data[lvl]['number_of_entries'] = int(meta_data[lvl]['number_of_entries']) + 1
        self.__write_meta(meta_data)
        return 0

    def reset_free_block_size(self, level) -> int:
        """
        Reset free block size at a particular level.
        :param level: level number at which free block size has to be reset
        :return: 0 on success, -1 on error
        """
        lvl = str(level)
        if not self.__level_exists(level):
            return -1
        meta_data = self.__get_meta()
        meta_data[lvl]['number_of_entries'] = 0
        self.__write_meta(meta_data)
        return 0

    def increase_level(self):
        """
        Increases the indexing level of customer data
        :return: None
        """
        from file_handler.indexer import Indexer

        customer_indexer = Indexer('customer')
        meta_data = self.__get_meta()
        new_level = int(meta_data['number_of_levels']) + 1
        old_level = new_level - 1
        new_level_dir = os.path.join(self.index_dir, str(new_level))
        meta_data[new_level] = INDEX_LEVEL_INIT
        meta_data['number_of_levels'] = new_level
        self.__write_meta(meta_data)
        if not os.path.isdir(new_level_dir):
            os.makedirs(new_level_dir, exist_ok=True)
        key1 = customer_indexer.get_starting_key('1.txt', old_level)
        key2 = customer_indexer.get_starting_key('2.txt', old_level)
        logging.debug(key1)
        customer_indexer.insert_index(new_level, key1, '1.txt')
        customer_indexer.insert_index(new_level, key2, '2.txt')

    def get_current_file(self, level) -> Union[str, int]:
        """
        Returns the current writing file at a given level, -1 if the level doesn't exists
        :param level: index level
        :return: current writing file
        """
        meta_data = self.__get_meta()
        lvl = str(level)
        return meta_data[lvl]['current_file_number'] + '.txt'

    def update_current_file(self, level) -> int:
        """
        Updates the current file number of the given level
        :param level: index level
        :return: 0 in success, -1 on error
        """
        lvl = str(level)
        if not self.__level_exists(level):
            return -1
        meta_data = self.__get_meta()
        new_file = int(meta_data[lvl]['current_file_number']) + 1
        meta_data[lvl]['current_file_number'] = str(new_file)
        self.__write_meta(meta_data)
        self.reset_free_block_size(level)
        return 0


if __name__ == '__main__':
    """
    Debugging block
    """
    # print(customer_index_meta.get_free_block_size(1))
    # customer_index_meta.increase_level()
    # customer_index_meta.decrement_free_block_size(1)
    print(customer_index_meta.get_current_file(1))
    print(customer_index_meta.update_current_file(1))
    print(customer_index_meta.get_current_file(1))

