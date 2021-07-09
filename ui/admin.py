import datetime
import tkinter as tk
from tkinter import *

class Admin:

    def init(self):
        pass

    @staticmethod
    def admin():
        """
        This method renders the window that lets admins to log into the system.
        This method call admin Log In handler when the admin clicks on log in button.
        """

        def log_in_admin():
            pass

        root = Tk()
        root.title('Admin Login')
        root.geometry('400x300')
        root.minsize(400, 300)
        root.maxsize(400, 300)
        login = Label(root, text="Log In")
        login.config(font=(44))
        login.grid(pady=(20, 0), padx=(170, 0), columnspan=3)

        admin_id = Label(root, text='Admin Id : ')
        admin_id_entry = Entry(root, width=30)
        admin_id.grid(row=3, pady=(40, 10), column=0, sticky=E)
        admin_id_entry.grid(row=3, pady=(40, 10), column=1, sticky=S)

        admin_pass = Label(root, text='Password : ')
        admin_pass_entry = Entry(root, width=30)
        admin_pass.grid(row=4, column=0, sticky=E)
        admin_pass_entry.grid(row=4, column=1, sticky=S)

        login_btn = Button(root, text='Login', command=log_in_admin)
        login_btn.grid(row=5, column=1, padx=(140, 0), pady=20)
        root.mainloop()

    @staticmethod
    def admin_control_panel():
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

        root = Tk()
        root.title('Admin Control Panel')
        root.geometry('400x300')
        root.minsize(400, 300)
        root.maxsize(400, 300)

        create_account = Button(root,text='Create New Account', padx=35, command=create_new_account_window)
        create_account.grid(pady=(100, 0), padx=(10,0), row=1,column=1, sticky=W)

        search_transact = Button(root, text='Search Transactions', padx=28, command=search_transaction_window)
        search_transact.grid(pady=(100,0), padx=(10,0), row=1, column=2,sticky=W)

        add_money = Button(root, text='Add Money', padx=59, command=add_money_window)
        add_money.grid(pady=(20,0), padx=(10,0), row=2, sticky=W, column=1)

        change_pass= Button(root, text='Change Passwords', padx=30, command=change_password_window)
        change_pass.grid(pady=(20,0), padx=(10,0), row=2, sticky=W, column=2)
        root.mainloop()


    @staticmethod
    def new_account():
        """
        Frame ID: 012
        This method renders window that lets admins create new user account.
        This method calls the account creation handler when the admin clicks on create account button.
        """

        def create_account():
            pass

    @staticmethod
    def search_transaction_admin():
        """
        Frame ID: 013
        This method renders window that lets admins search transaction history of different users.
        This method calls transaction searcher when the user clicks on search button.
        """

        def search_transaction():
            pass

    @staticmethod
    def deposit_withdraw_money(op_type: int):
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
    Admin.admin()
    Admin.admin_control_panel()