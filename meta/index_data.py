import json
import sys

from constants import *

sys.path.append('/...')


class CustomerData:

    @staticmethod
    def get_free_block_size(index_meta_file, level):
        """
        :param index_meta_file: Location of index meta file
        :param level: Index level number
        :return: number of records that could be inserted to the level without
        causing an overflow. -1 if level doesn't exists
        """
        lvl = str(level)
        with open(index_meta_file) as meta_file:
            meta_data = json.load(meta_file)
        highest_level = meta_data.get('number_of_levels', 0)
        if level > highest_level:
            return -1
        return BLOCK_SIZE - meta_data[lvl]['number_of_entries']

    @staticmethod
    def increase_level():
        """
        Increases the indexing level of customer data
        :return: None
        """


if __name__ == '__main__':
    customer_meta_file = os.path.join(CUSTOMER_META_DIRECTORY, 'meta.json')
    print(CustomerData.get_free_block_size(customer_meta_file, 1))
