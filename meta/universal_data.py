import json
import os
from constants import *
import sys

sys.path.append('/...')
universal_meta_file_path = os.path.join(META_DIRECTORY, 'universal_data.json')


class UniversalData:

    @staticmethod
    def get_next_account_number() -> int:
        """
        :return: Next possible account number.
        """
        with open(universal_meta_file_path) as data_file:
            data = json.load(data_file)
        return data['next_account_number']

    @staticmethod
    def get_current_customer_account_file() -> str:
        """
        :return: file name of the latest file to write the customer account details to.
        """
        with open(universal_meta_file_path) as data_file:
            data = json.load(data_file)
        return data['current_customer_account_file']

    @staticmethod
    def update_next_account_number() -> None:
        """
        This method updates the next available account number by 1.
        :return: None
        """
        with open(universal_meta_file_path) as data_file:
            data = json.load(data_file)
        data['next_account_number'] = str(int(data.get('next_account_number', 0)) + 1)
        with open(universal_meta_file_path, 'w') as data_file:
            json.dump(data, data_file)

    @staticmethod
    def update_current_account_file(file_name: str) -> None:
        """
        This method updates the name of the current file that stores customer account details.
        :param file_name: latest file name to be set as the current account file
        :return: None
        """
        pass


if __name__ == '__main__':
    """
    Initial setup
    """

    universal_data = {
        'next_account_number': '1',
        'current_customer_account_file': 'data1.txt'
    }

    uni_data_file = open(universal_meta_file_path, 'w')
    json.dump(universal_data, uni_data_file)
    uni_data_file.close()
