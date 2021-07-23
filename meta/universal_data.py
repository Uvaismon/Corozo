import json
import os
from constants import *
universal_meta_file_path = os.path.join(META_DIRECTORY, 'universal_data.json')


class UniversalData:

    def __init__(self, user):
        self.user = user

    def __get_meta(self) -> dict:
        """
        :return: return meta data as a dict
        """
        with open(universal_meta_file_path) as data_file:
            meta_data = json.load(data_file)[self.user]
        return meta_data

    def __write_meta(self, meta_data) -> None:
        """
        This method write data to the meta file.
        :param meta_data: Data to be written to the meta file
        :return:
        """
        with open(universal_meta_file_path) as data_file:
            data = json.load(data_file)
        data[self.user] = meta_data
        with open(universal_meta_file_path, 'w') as data_file:
            json.dump(data, data_file)

    def get_next_account_number(self) -> int:
        """
        :return: Next possible account number.
        """
        meta_data = self.__get_meta()
        return meta_data['next_account_number']

    def get_current_account_file(self) -> str:
        """
        :return: file name of the latest file to write the user account details to.
        """
        meta_data = self.__get_meta()
        return meta_data['current_account_file'] + '.txt'

    def update_next_account_number(self) -> None:
        """
        This method updates the next available account number by 1.
        :return: None
        """
        meta_data = self.__get_meta()
        meta_data['next_account_number'] = str(int(meta_data.get('next_account_number', 0)) + 1)
        self.__write_meta(meta_data)

    def update_current_account_file(self) -> None:
        """
        This method updates the name of the current file that stores user account details to one file higher.
        :return: None
        """
        meta_data = self.__get_meta()
        meta_data['current_account_file'] = str(int(meta_data['current_account_file']) + 1)
        self.__write_meta(meta_data)
        self.reset_block_size()

    def get_free_block_size(self) -> int:
        """
        :return: returns free space remaining in current block
        """
        meta_data = self.__get_meta()
        return BLOCK_SIZE - int(meta_data['number_of_entries'])

    def decrement_free_block_size(self) -> None:
        """
        Updates the number of entries in the current user account file.
        :return:
        """
        meta_data = self.__get_meta()
        meta_data['number_of_entries'] = int(meta_data['number_of_entries']) + 1
        self.__write_meta(meta_data)

    def reset_block_size(self) -> None:
        """
        This method is used to reset the block.
        Usually called when a new block is created.
        :return: None
        """
        meta_data = self.__get_meta()
        meta_data['number_of_entries'] = '0'
        self.__write_meta(meta_data)


# Universal data initialization
def initialize() -> None:
    """
    Initilize Universal meta file.
    :return: None
    """
    universal_data = {
        'customer': {
            'next_account_number': '1',
            'current_account_file': '1',
            'number_of_entries': '0'
        },
        'admin': {
            'next_account_number': '1',
            'current_account_file': '1',
            'number_of_entries': '0'
        },
        'transactor': {
            'next_account_number': '1',
            'current_account_file': '1',
            'number_of_entries': '0'
        }
    }

    with open(universal_meta_file_path, 'w') as uni_data_file:
        json.dump(universal_data, uni_data_file)
