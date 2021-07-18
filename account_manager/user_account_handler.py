import datetime
import re
from file_handler import *
from file_handler.read_write import DELETION_INDICATOR
from meta import *
from constants import *

import sys

sys.path.append('/...')


class UserAccountFileHandler:

    def __init__(self, user):
        self.user = user
        if user == 'customer':
            self.universal_data = universal_customer_data
            self.data_dir = CUSTOMER_DATA_DIRECTORY
            self.indexer = customer_indexer
        if user == 'admin':
            self.universal_data = universal_admin_data
            self.data_dir = ADMIN_DATA_DIRECTORY
            self.indexer = admin_indexer

    def __get_data_list(self, data) -> list:
        """
        :param: Dictionary of data to be stored
        :return: List of user data to be stored in file
        """
        data_list = []
        if not data.get('creation_date', False):
            data['creation_date'] = str(datetime.datetime.now())
        if data.get('account_number', -1) == -1:
            data['account_number'] = self.universal_data.get_next_account_number()
        if data.get('balance', -1) == -1:
            data['balance'] = 0
        data['password'] += ' ' * (PASSWORD_SIZE - len(data['password']))
        data['balance'] = str(data['balance'])
        data['balance'] = ('0' * (MAX_DIGITS - len(data['balance']))) + data['balance']
        if self.user == 'customer':
            data_list = [
                str(data['account_number']),
                data['password'],
                data['account_holder_name'],
                data['account_type'],
                data['creation_date'],
                data['balance']
            ]

        if self.user == 'admin':
            data_list = [
                str(data['account_number']),
                data['password'],
                data['account_holder_name'],
                data['creation_date']
            ]
        return data_list

    def __get_data_dict(self, data_list: list) -> dict:
        """
        :param data_list: Data as a list
        :return: return user data as dictionary.
        """
        if self.user == 'customer':
            return {
                'account_number': int(data_list[0]),
                'password': data_list[1].strip(),
                'account_holder_name': data_list[2],
                'account_type': data_list[3],
                'creation_date': data_list[4],
                'balance': int(data_list[5].strip())
            }

    def __fetch_record(self, file_name: str, offset: int) -> dict:
        """
        :param file_name: Name of the file to fetch record from
        :param offset: file offset where the record in present
        :return: dictionary containing user data. Empty dictionary if user doesn't exists.
        """
        data_list = ReadWrite.file_reader(
            file_name=file_name, dir_path=self.data_dir, offset=offset, number_or_records=1)
        if not data_list:
            return {}
        return self.__get_data_dict(data_list[0])

    def create_account(self, **data_list) -> None:
        """
        This method handles the account creation process.
        :param data_list: Dictionary of data related to the customer
        :return: None
        """

        account_number = self.universal_data.get_next_account_number()
        if self.universal_data.get_free_block_size() < 1:
            self.universal_data.update_current_account_file()
        file_name = self.universal_data.get_current_account_file()

        index = ReadWrite.insert(file_name,
                                 self.data_dir,
                                 self.__get_data_list(data_list)
                                 )
        self.indexer.insert_index(1, str(account_number), str(index))

        self.universal_data.update_next_account_number()
        self.universal_data.decrement_free_block_size()

    def delete_account(self, account_number: int) -> None:
        """
        This method is used to delete or close a user account.
        :param account_number: Account number of the account to be deleted.
        :return: None
        """
        index = self.indexer.fetch_index(account_number)
        if not index:
            return
        file_name = index[0]
        offset = index[1]
        ReadWrite.file_writer(file_name, self.data_dir, DELETION_INDICATOR, offset)

    def authenticate(self, account_number: int, password: str) -> dict:
        """
        This method is used to authenticate the customers.
        :param account_number: account number of the customer
        :param password: password of the customer
        :return: Account details as a dict if authenticated successfully, empty dict otherwise.
        """
        index = self.indexer.fetch_index(account_number)
        if not index:
            return {}
        record = self.__fetch_record(index[0], index[1])
        if not record:
            return {}
        if record['password'] == password:
            del (record['password'])
            return record
        return {}

    def update_balance(self, account_number: int, update_amount):
        """
        Updates account balance of the user.
        :param account_number: account number of the user
        :param update_amount: amount to be deposited(if positive) or deducted(if negative) from the account.
        """
        file_name, offset = self.indexer.fetch_index(account_number)
        data_dict = self.__fetch_record(file_name, offset)
        data_dict['balance'] = str(data_dict['balance'] + update_amount)
        new_rec = ReadWrite.pack(self.__get_data_list(data_dict))
        ReadWrite.file_writer(file_name, self.data_dir, new_rec, offset)

    def get_balance(self, account_number) -> int:
        """
        :param account_number: Account number of the user
        :return: Balance of the given account.
        """
        file_name, offset = self.indexer.fetch_index(account_number)
        data_dict = self.__fetch_record(file_name, offset)
        return data_dict['balance']

    def change_password(self, account_number, new_password):
        """
        Updates the user account password
        :param account_number: Account number of the user
        :param new_password: New password to be updated in place of the old password
        :return: None
        """
        file_name, offset = self.indexer.fetch_index(account_number)
        data_dict = self.__fetch_record(file_name, offset)
        data_dict['password'] = new_password
        new_rec = ReadWrite.pack(self.__get_data_list(data_dict))
        ReadWrite.file_writer(file_name, self.data_dir, new_rec, offset)

    @staticmethod
    def pass_strength(password):
        """ This function will take password as argument and returns 1 if password is strong else returns 0"""

        al_s = re.search(r'[a-z]', password)
        al_b = re.search(r'[A-Z]', password)
        num = re.search(r'[0-9]', password)
        spec = re.search(r'[^a-zA-Z0-9]', password)

        strength = al_s and al_b and num and spec and 6 <= len(password) <= 10

        if strength:
            return 1
        else:
            return 0


if __name__ == '__main__':
    """
    Debugging area
    """
    # print(UserAccountFileHandler('customer').authenticate(9, '9510'))
    # UserAccountFileHandler('customer').delete_account(25)
    # UserAccountFileHandler('customer').update_balance(2, 100)
    # UserAccountFileHandler('customer').change_password(3, 'SicMu2@')
