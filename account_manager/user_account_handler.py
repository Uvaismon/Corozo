import datetime
import re
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

    def __get_data_dict(self, data_list: list) -> dict:
        """
        :param data_list: Data as a list
        :return: return user data as dictionary.
        """
        if self.user == 'customer':
            return {
                'account_number': data_list[0],
                'password': data_list[1],
                'account_holder_name': data_list[2],
                'account_type': data_list[3],
                'creation_date': data_list[4],
                'balance': data_list[5]
            }

    def __fetch_record(self, file_name: str, offset: int) -> dict:
        """
        :param file_name: Name of the file to fetch record from
        :param offset: file offset where the record in present
        :return: dictionary containing user data.
        """
        data_list = ReadWrite.file_reader(
            file_name=file_name, dir_path=self.data_dir, offset=offset, number_or_records=1)
        return self.__get_data_dict(data_list)

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

    def update_balance(self, account_number: int, update_amount) -> int:
        """
        Updates account balance of the user.
        :param account_number: account number of the user
        :param update_amount: amount to be deposited(if positive) or deducted(if negative) from the account.
        :return: 1 if successfully updated, 0 otherwise.
        """
        pass

    @staticmethod
    def pass_strength(password):
        """ This function will take password as argument and returns 1 if password is strong else returns 0"""

        expression = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{4,10}$"
        cond = re.compile(expression)

        strength = re.search(cond, password)
        if strength:
            return 1
        else:
            return 0


if __name__ == '__main__':
    """
    Debugging area
    """
