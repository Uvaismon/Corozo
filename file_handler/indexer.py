from meta import *
from file_handler.read_write import ReadWrite
from constants import *


class Indexer:

    def __init__(self, user):
        """
        Initializes the class according to the user.
        :param user: customer or admin
        :return: None
        """
        if user == 'customer':
            self.user_meta_obj = customer_index_meta
            self.dir_path = CUSTOMER_INDEX_DIRECTORY

        if user == 'admin':
            self.user_meta_obj = admin_index_meta
            self.dir_path = ADMIN_INDEX_DIRECTORY

    def __get_level_path(self, level) -> str:
        """
        :param level: Index level
        :return: Path to the given level.
        """
        return os.path.join(self.dir_path, str(level))

    def insert_index(self, level, key, pointer) -> None:
        """
        Registers the index of the given key.
        :param level: Indexing level
        :param key: key for which index has to be build
        :param pointer: offset of the key
        :return:
        """
        new_file = False
        free_block_size = self.user_meta_obj.get_free_block_size(level)
        if not free_block_size:
            self.user_meta_obj.update_current_file(level)
            new_file = True
        file_name = self.user_meta_obj.get_current_file(level)
        if level == 1:
            data_file = universal_customer_data.get_current_account_file()
            data_list = [
                key,
                data_file,
                pointer
            ]
        else:
            data_list = [
                key,
                pointer
            ]

        ReadWrite.insert(file_name, self.__get_level_path(level), data_list)
        self.user_meta_obj.decrement_free_block_size(level)
        if file_name == '2.txt' and new_file:
            self.user_meta_obj.increase_level()
        elif new_file:
            self.get_starting_key(file_name, level)
            self.insert_index(level + 1, key, file_name)

    def fetch_index(self, key: int, level: int = None, file_name: str = '1.txt') -> list:
        """
        Fetch the record location of the given key
        :param key: key of the record to be searched
        :param level: indexing level
        :param file_name: index file name
        :return: record location as a list as [file_name, offset]. Return empty list if the key doesn't exists.
        """
        if not level:
            level = self.user_meta_obj.get_highest_level()
        index_loc = os.path.join(self.dir_path, str(level))
        records = ReadWrite.file_reader(file_name, index_loc)
        record_number = -1
        low_key = int(records[0][0])
        for record in records:
            if int(record[0]) <= key:
                low_key = int(record[0])
                record_number += 1
            else:
                break
        if len(records[record_number]) == 2:
            return self.fetch_index(key, level - 1, records[record_number][1])
        if low_key != key:
            return []
        return [records[record_number][1], int(records[record_number][2])]

    def get_starting_key(self, file_name, level) -> str:
        """
        Returns the first key in a file.
        :param level: Indexing level
        :param file_name: Name of the file to fetch the key from.
        :return: first key of the file
        """
        dir_path = self.__get_level_path(level)
        data = ReadWrite.file_reader(file_name=file_name, dir_path=dir_path, number_or_records=1)[0]
        data_list = ReadWrite.unpack(data)
        return data_list[0]


if __name__ == '__main__':
    """
    Debugging area
    """
    k = Indexer('customer').fetch_index(1)
    print(k)
