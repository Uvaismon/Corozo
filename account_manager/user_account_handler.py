import datetime

from meta import *
from file_handler import *
from constants import *

import sys

sys.path.append('/...')


class UserAccountFileHandler:

    @staticmethod
    def create_account(account_holder_name: str, account_type: str, password: str) -> None:
        """
        This method handles the account creation process.
        :param account_holder_name: account_holder_name
        :param account_type: savings or current
        :param password: initial password of account holder
        :return: None
        """

        account_number = universal_customer_data.get_next_account_number()
        creation_date = str(datetime.datetime.now())
        balance = '0' * MAX_DIGITS
        if universal_customer_data.get_free_block_size() < 1:
            universal_customer_data.update_current_account_file()
            universal_customer_data.reset_block_size()
        file_name = universal_customer_data.get_current_account_file()

        index = ReadWrite.insert(file_name,
                                 [account_number,
                                  account_holder_name,
                                  account_type,
                                  creation_date,
                                  balance,
                                  password]
                                 )
        print(index)

        universal_customer_data.update_next_account_number()
        universal_customer_data.decrement_free_block_size()

    @staticmethod
    def delete_account(account_number: int) -> None:
        """
        This method is used to delete or close a user account.
        :param account_number: Account number of the account to be deleted.
        :return: None
        """
        pass

    @staticmethod
    def authenticate(account_number: int, password: str):
        """
        This method is used to authenticate the customers.
        :param account_number: account number of the customer
        :param password: password of the customer
        :return: 1 if credentials are matched, 0 otherwise.
        """
        pass

    @staticmethod
    def update_balance(account_number: int, update_amount) -> int:
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
    UserAccountFileHandler.create_account('Tester1', 'current', 'abc456')
    UserAccountFileHandler.create_account('Tester2', 'savings', 'dfsf5454')
    UserAccountFileHandler.create_account('Tester3', 'current', 'sdfd1202')
