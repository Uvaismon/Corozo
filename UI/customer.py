import datetime
import tkinter as tk


class Customer:

    def __init__(self):
        pass

    def log_in(self) -> (str, str):
        """
        pull-push
        Frame ID: 001
        This method renders a log in window. Returns a tuple consisting of 2 strings in the following order.
        (acct_number, password)
        """
        pass

    def home(self, account_number: int, acct_holder_name: str, acct_type: str, balance: float) -> int:
        """
        Frame ID: 002
        This method renders the home window. It takes in the following arguments.
        account number -> int,
        account holder name -> str,
        account type -> [Savings, Current],
        account balance -> float.
        The window provides 2 choices to the users.
        The return value is a 0 or 1 depending on the choice selected by the user.
        Transact -> 0,
        Settings -> 1
        """
        pass

    def settings(self) -> int:
        """
        Frame ID: 003
        This method renders the account settings window.
        It provides 2 choices to the users. The return value is a 0 or 1 depending on the choice selected by the user.
        Change password -> 0,
        Close account -> 1
        """
        pass

    def transact(self) -> int:
        """
        Frame ID: 004
        This method render the transaction window. The user will be given 3 options.
        The return value of the method depends on the option selected by the user.
        Account Statement -> 0,
        Search Transaction -> 1,
        Send money -> 2
        """
        pass

    def change_password(self) -> (str, str):
        """
        Frame ID: 005
        This method renders window that lets users to change password.
        Return value is a 2 elements tuple consisting of the ols password and new password in the following order.
        (old_password, new_password)
        """
        pass

    def close_account(self, acct_number: int, balance: float) -> str:
        """
        Frame ID: 006
        This method renders the close account window. It takes in the following arguments.
        account number -> int,
        account balance -> float
        It returns the password as a string entered by the user as a confirmation to close their account.
        """
        pass

    def account_statement(self, acct_number: int, acct_type: str, trans_list: list) -> None:
        """
        Frame ID: 007
        This method renders the window that displays the users account statement.
        It takes in the following arguments.
        account number -> int,
        account type -> str
        transaction list -> list of transactions
        This method does not return any value.
        """
        pass

    def search_transactions(self) -> (datetime.date, datetime.date, int):
        """
        Frame ID: 008
        This method renders the window that displays the that lets users filter their transactions based on time
        period and type of transaction.
        It return a tuple with 3 elements as follows.
        (from_date, to_date, type)
        from -> datetime.date
        to -> datetime.date
        type -> 0 (if the type is deposit), 1 (if the type is withdrawal)
        """
        pass

    def send_money(self) -> (int, float):
        """
        Frame ID: 009
        This method renders the window that lets users send money to another account.
        This method returns the account number and the amount to be transferred as follows.
        (account_number, balance)
        account_number -> int
        balance -> float
        """
        pass


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """
