import datetime

from meta import *
from file_handler import *

import sys

sys.path.append('/...')


class AccountFileHandler:

    @staticmethod
    def create_account(account_holder_name: str, account_type: str, password: str) -> None:
        """
        This method handles the account creation process.
        :param account_holder_name: account_holder_name
        :param account_type: savings or current
        :param password: initial password of account holder
        :return: None
        """

        account_number = UniversalData.get_next_account_number()
        creation_date = str(datetime.datetime.now())
        file_name = UniversalData.get_current_customer_account_file()
        balance = '0'

        index = ReadWrite.insert(file_name,
                                 [account_number,
                                  account_holder_name,
                                  account_type,
                                  creation_date,
                                  balance,
                                  password]
                                 )
        UniversalData.update_next_account_number()


if __name__ == '__main__':
    """
    Debugging area
    """
    AccountFileHandler.create_account('Tester1', 'current', 'abc456')
    AccountFileHandler.create_account('Tester2', 'savings', 'dfsf5454')
    AccountFileHandler.create_account('Tester3', 'current', 'sdfd1202')
