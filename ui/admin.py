import datetime
import tkinter as tk


class Admin:

    def __init__(self):
        pass

    def admin(self) -> (str, str):
        """
        This method renders the window that lets admins to log into the system.
        It returns a tuple that consist of 2 strings in the following order.
        (admin_id, password)
        admin_in -> int,
        password -> str
        """
        pass

    def admin_control_panel(self) -> int:
        """
        Frame ID: 011
        This method renders window that lets admins perform various operations as mentioned in the docs.
        It returns an integer value as per the option selected by admin as follows.
        create new account -> 0,
        search transaction -> 1,
        add money -> 2,
        change password -> 3
        """
        pass

    def new_account(self) -> (str, str, str):
        """
        Frame ID: 012
        This method renders window that lets admins create new user account. It returns user name, type of account and
        account password as a tuple as follows.
        (user_name, acct_type, password)
        user name -> str,
        account type -> str,
        password -> str
        """
        pass

    def search_transaction_admin(self) -> (int, datetime.date, datetime.date):
        """
        Frame ID: 013
        This method renders window that lets admins search transaction history of different users.
        It returns the account number, from date and to date as a tuple as follows.
        (acct_number, from_date, to_date)
        account  number -> int,
        from_date -> datetime.date,
        to_date -> datetime.date
        """
        pass

    def deposit_withdraw_money(self, op_type: int) -> (int, float, str):
        """
        This method renders the window that lets admin handle deposits and withdrawal.
        If op_type is 0, amount is deposited to the user account.
        If op_type is 1, amount is withdrawn from user account.
        It return the account number, amount to be added and the admin account password for security as a tuple as
        follows.
        (acct_number, amount, password)
        account number -> int
        amount -> float
        password -> str
        """
        pass


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """
