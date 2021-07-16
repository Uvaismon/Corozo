import datetime

from file_handler import *
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
        creation_date = str(datetime.datetime.now())
        balance = '0' * MAX_DIGITS
        if self.user == 'customer':
            data_list = [
                self.universal_data.get_next_account_number(),
                data['password'],
                data['account_holder_name'],
                data['account_type'],
                creation_date,
                balance
            ]

        if self.user == 'admin':
            data_list = [
                self.universal_data.get_next_account_number(),
                data['password'],
                data['account_holder_name'],
                creation_date
            ]
        return data_list

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
        pass

    def authenticate(self, account_number: int, password: str):
        """
        This method is used to authenticate the customers.
        :param account_number: account number of the customer
        :param password: password of the customer
        :return: 1 if credentials are matched, 0 otherwise.
        """
        pass

    def update_balance(self, account_number: int, update_amount) -> int:
        """
        Updates account balance of the user.
        :param account_number: account number of the user
        :param update_amount: amount to be deposited(if positive) or deducted(if negative) from the account.
        :return: 1 if successfully updated, 0 otherwise.
        """
        pass


if __name__ == '__main__':
    """
    Debugging area
    """
