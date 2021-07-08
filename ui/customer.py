import datetime
import tkinter as tk


class Customer:

    def __init__(self):
        pass

    @staticmethod
    def log_in(self):
        """
        pull-push
        Frame ID: 001
        This method renders a log in window.
        This method calls the login handler when the user clicks Log In button and
            Admin portal handler if user clicks admin button.
        """

        def log_in():
            pass

        def admin():
            pass

    @staticmethod
    def home(account_number: int, acct_holder_name: str, acct_type: str, balance: float):
        """
        Frame ID: 002
        This method renders the home window. It takes in the following arguments.
        account number -> int,
        account holder name -> str,
        account type -> [Savings, Current],
        account balance -> float.
        The window provides 2 choices to the users.
        The method calls transaction handler if user clicks transact button and settings handler
            if user clicks settings button.
        """

        def transact():
            pass

        def settings():
            pass

    @staticmethod
    def settings(self):
        """
        Frame ID: 003
        This method renders the account settings window.
        It provides 2 choices to the users.
        The method calls password changing window if users clicks change password button and account closing window
            if user clicks close account button.
        """

        def change_password_window():
            pass

        def close_account_window():
            pass

    @staticmethod
    def transact(self):
        """
        Frame ID: 004
        This method render the transaction window. The user will be given 3 options.
        The is method calls account statement manager if user clicks on account statement button,
            transaction searching window if user clicks on search transaction button and
            money sending window if user clicks on send money button.
        """

        def account_statement():
            pass

        def search_transaction_window():
            pass

        def send_money_window():
            pass

    @staticmethod
    def change_password():
        """
        Frame ID: 005
        This method renders window that lets users to change password.
        This method calls password changer when user clicks submit button to change password.
        """

        def change_password():
            pass

    @staticmethod
    def close_account(self, acct_number: int, balance: float):
        """
        Frame ID: 006
        This method renders the close account window. It takes in the following arguments.
        account number -> int,
        account balance -> float
        This method calls close account manager if user chooses to close account:
        """

        def close_account():
            pass

    @staticmethod
    def account_statement(self, acct_number: int, acct_type: str, trans_list: list):
        """
        Frame ID: 007
        This method renders the window that displays the users account statement.
        It takes in the following arguments.
        account number -> int,
        account type -> str
        transaction list -> list of transactions
        """
        pass

    @staticmethod
    def search_transactions(self):
        """
        Frame ID: 008
        This method renders the window that displays that lets users filter their transactions based on time
        period and type of transaction.
        This method calls transaction filtering window.
        """

        def filter_transaction():
            pass

    @staticmethod
    def send_money(self) -> (int, float):
        """
        Frame ID: 009
        This method renders the window that lets users send money to another account.
        This method calls money sending handler.
        """

        def send_money():
            pass


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """
