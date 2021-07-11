import datetime
import tkinter as tk
from tkinter import *


class Customer:

    def __init__(self):
        pass

    @staticmethod
    def log_in():
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

        root = Tk()
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)
        root.title("Login")
        # welcome = Label(root, text="Welcome to Avocado Crypt", font=('Times New Roman', 24), fg='Red', width=80)

        account_number = Label(root, text="Enter Account Number")

        e = Entry(root, width=30)

        Passcode = Label(root, text="Enter Passcode: ")
        e2 = Entry(root, width=30)

        account_number.grid(row=1, column=0)
        e.grid(row=1, column=1, padx=10, pady=10)

        Passcode.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        my_button = Button(root, text="LOGIN", command=log_in)
        my_button.grid(row=3, column=1)
        # welcome.grid(row=0, column=0)

        Admin_Button = Button(root, text="ADMIN", command=admin())
        Admin_Button.grid(row=4, column=3)

        root.mainloop()

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

        root = Tk()
        root.geometry("400x400")
        root.minsize(400, 400)
        root.maxsize(400, 400)
        root.title("Home")

        AccountNumber = Label(root, text="Enter Account Number")

        e1 = Label(root, text=account_number, width=30)

        Accountholdername = Label(root, text="Enter Name: ")
        e2 = Label(root, text=acct_holder_name, width=30)

        AccountNumber.grid(row=1, column=0)
        e1.grid(row=1, column=1, padx=10, pady=10)

        Accountholdername.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        Accounttype = Label(root, text="Choose account type")

        e3 = Label(root, text=acct_type, width=30)

        AccountBalance = Label(root, text="The balance is: ")
        e4 = Label(root, text=balance, width=30)

        Accounttype.grid(row=3, column=0)
        e3.grid(row=3, column=1, padx=10, pady=10)

        AccountBalance.grid(row=4, column=0)
        e4.grid(row=4, column=1, padx=10, pady=10)

        transact = Button(root, text="Transact", command=transact)
        transact.grid(row=6, column=0)
        settings = Button(root, text="Settings", command=settings)
        settings.grid(row=6, column=1)

        root.mainloop()

    @staticmethod
    def settings():
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

        root = Tk()
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)

        def Change_password():
            Change_password()

        def close_account():
            close_account()

        Change_password = Button(root, text="Change Password", command=Change_password)
        Change_password.grid(row=1, column=0, padx=20, pady=15)

        close_account = Button(root, text="Close Account", command=close_account)
        close_account.grid(row=2, column=0, padx=20, pady=15)

        root.mainloop()

    @staticmethod
    def transact():
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

        root = Tk()
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)

        account_statement = Button(root, text="Account Statement", command=account_statement)
        account_statement.grid(row=1, column=0, padx=20, pady=15)

        search_transaction_window = Button(root, text="Search Transaction", command=search_transaction_window)
        search_transaction_window.grid(row=2, column=0, padx=20, pady=15)

        send_money_window = Button(root, text="Send Money", command=send_money_window)
        send_money_window.grid(row=3, column=0, padx=20, pady=15)

        root.mainloop()

    @staticmethod
    def change_password():
        """
        Frame ID: 005
        This method renders window that lets users to change password.
        This method calls password changer when user clicks submit button to change password.
        """

        def change_password():
            pass

        root = Tk()
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)

        enter_old_passcode = Label(root, text="Enter Old Passcode")

        e = Entry(root, width=30)

        enter_new_passcode = Label(root, text="Enter New Passcode: ")
        e2 = Entry(root, width=30)

        reenter_new_passcode = Label(root, text="Re-enter New Passcode")
        e3 = Entry(root, width=30)

        enter_old_passcode.grid(row=1, column=0)
        e.grid(row=1, column=1, padx=10, pady=10)

        enter_new_passcode.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        reenter_new_passcode.grid(row=3, column=0)
        e3.grid(row=3, column=1, padx=10, pady=10)

        submit = Button(root, text="Submit", command=change_password)
        submit.grid(row=4, column=0, padx=30, pady=15)

        root.mainloop()

    @staticmethod
    def close_account(acct_number: int, balance: float):
        """
        Frame ID: 006
        This method renders the close account window. It takes in the following arguments.
        account number -> int,
        account balance -> float
        This method calls close account manager if user chooses to close account:
        """

        def close_account():
            pass

        root = Tk()

        Account_Number = 12345
        Account_Balance = 1220
        password = "xyzxyz"

        AccountNumber = Label(root, text="Enter Account Number")

        e1 = Label(root, text=Account_Number, width=30)

        AccountBalance = Label(root, text="Account Balance is : ")
        e2 = Label(root, text=Account_Balance, width=30)

        Password = Label(root, text="Enter Password")
        e3 = Entry(root, width=30)

        AccountNumber.grid(row=1, column=0)
        e1.grid(row=1, column=1, padx=10, pady=10)

        AccountBalance.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        Password.grid(row=3, column=0)
        e3.grid(row=3, column=1, padx=10, pady=10)



        close_account = Button(root, text="Close", command=close_account)
        close_account.grid(row=4, column=0, padx=30, pady=15)

        root.mainloop()

    @staticmethod
    def account_statement(acct_number: int, acct_type: str, trans_list: list):
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
    def search_transactions():
        """
        Frame ID: 008
        This method renders the window that displays that lets users filter their transactions based on time
        period and type of transaction.
        This method calls transaction filtering window.
        """

        def filter_transaction():
            pass

    @staticmethod
    def send_money():
        """
        Frame ID: 009
        This method renders the window that lets users send money to another account.
        This method calls money sending handler.
        """

        def send_money():
            pass

        root = Tk()



        AccountNumber = Label(root, text="Enter Account Number")

        e1 = Entry(root, width=30)

        Amount = Label(root, text="Enter Amount")

        e2 = Entry(root, width=30)

        AccountNumber.grid(row=1, column=0)
        e1.grid(row=1, column=1, padx=10, pady=10)

        Amount.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        send = Button(root, text="Send", command=send_money)
        send.grid(row=3, column=0, padx=10, pady=10)

        root.mainloop()

if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """

    Customer.log_in()
    Customer.home(1234, "zabi", "Savings", 5000)
    Customer.settings()
    Customer.transact()
    Customer.change_password()
    Customer.close_account(1234, 2000)
    Customer.send_money()