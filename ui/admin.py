import datetime
import tkinter as tk


class Admin:

    def __init__(self):
        pass

    @staticmethod
    def admin(self):
        """
        This method renders the window that lets admins to log into the system.
        This method call admin Log In handler when the admin clicks on log in button.
        """

        def log_in_admin():
            pass

    @staticmethod
    def admin_control_panel(self):
        """
        Frame ID: 011
        This method renders window that lets admins perform various operations as mentioned in the docs.
        This method calls account creation window if the admin clicks on create account button, search transaction
            window if the admin clicks on search transaction button, money adding window if the admin clicks on
            add money button and password changer if the user clicks on change password button.
        """

        def create_new_account_window():
            pass

        def search_transaction_window():
            pass

        def add_money_window():
            pass

        def change_password_window():
            pass

    @staticmethod
    def new_account(self):
        """
        Frame ID: 012
        This method renders window that lets admins create new user account.
        This method calls the account creation handler when the admin clicks on create account button.
        """

        def create_account():
            pass

    @staticmethod
    def search_transaction_admin(self):
        """
        Frame ID: 013
        This method renders window that lets admins search transaction history of different users.
        This method calls transaction searcher when the user clicks on search button.
        """

        def search_transaction():
            pass

    @staticmethod
    def deposit_withdraw_money(self, op_type: int):
        """
        Frame ID: 014
        This method renders the window that lets admin handle deposits and withdrawal.
        If op_type is 0, amount is deposited to the user account.
        If op_type is 1, amount is withdrawn from user account.
        It calls the deposit handler if admin clicks on add money button and calls withdrawal handler if the admin
            clicks on withdraw button.
        """

        def withdraw():
            pass

        def deposit():
            pass


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """
