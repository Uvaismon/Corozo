import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkcalendar import *
from file_handler import ReadWrite
from account_manager.user_account_handler import UserAccountFileHandler
import sys

sys.path.append('/...')


class Admin:

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
        login.config(font=44)
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

        create_account = Button(root, text='Create New Account', padx=35, command=create_new_account_window)
        create_account.grid(pady=(100, 0), padx=(10, 0), row=1, column=1, sticky=W)

        search_transact = Button(root, text='Search Transactions', padx=28, command=search_transaction_window)
        search_transact.grid(pady=(100, 0), padx=(10, 0), row=1, column=2, sticky=W)

        add_money = Button(root, text='Add Money', padx=59, command=add_money_window)
        add_money.grid(pady=(20, 0), padx=(10, 0), row=2, sticky=W, column=1)

        change_pass = Button(root, text='Change Passwords', padx=30, command=change_password_window)
        change_pass.grid(pady=(20, 0), padx=(10, 0), row=2, sticky=W, column=2)
        root.mainloop()

    @staticmethod
    def new_account():
        """
        Frame ID: 012
        This method renders window that lets admins create new user account.
        This method calls the account creation handler when the admin clicks on create account button.
        """

        def create_account():
            account_holder_name = name_entry.get()
            account_type = items.get()
            password = pass_entry.get()
            UserAccountFileHandler.create_account(account_holder_name, account_type, password)
            root.destroy()

        root = Tk()
        root.title('New Account')
        root.geometry('400x300')
        root.minsize(400, 300)
        root.maxsize(400, 300)

        name = Label(root, text='Name :')
        name_entry = Entry(root)
        name.grid(pady=(30, 0), padx=(20, 0), column=1, row=1, sticky=E)
        name_entry.grid(pady=(30, 0), padx=(20, 0), column=2, row=1, sticky=W)

        acnt_type = Label(root, text='Account Type :')
        acnt_type.grid(pady=(10, 0), padx=(20, 0), column=1, row=2, sticky=E)

        items = StringVar(root, '1')
        values = {
            "Current": 'current',
            "Savings": 'savings'
        }
        i = 2
        for (text, value) in values.items():
            Radiobutton(root, text=text, variable=items, value=value).grid(pady=(10, 0), padx=(20, 0), column=i, row=2,
                                                                           sticky=W)
            i = i + 1

        acnt_pass = Label(root, text='Password :')
        pass_entry = Entry(root)
        acnt_pass.grid(pady=(10, 0), padx=(20, 0), column=1, row=4, sticky=E)
        pass_entry.grid(pady=(10, 0), padx=(20, 0), column=2, row=4, sticky=W)

        create_btn = Button(root, text='Create', command=create_account)
        create_btn.grid(columnspan=4, pady=(30, 0), padx=(50, 0))
        root.mainloop()

    @staticmethod
    def search_transaction_admin():
        """
        Frame ID: 013
        This method renders window that lets admins search transaction history of different users.
        This method calls transaction searcher when the user clicks on search button.
        """

        def search_transaction():
            pass

        root = Tk()
        root.title('Search Transactions(Admin)')
        root.geometry('500x300')
        root.minsize(500, 300)
        root.maxsize(500, 400)

        def select_date(i):
            root.geometry('600x400')
            cal = Calendar(root, selectmode='day', year=2021, month=7, day=15)
            if i == 0:
                cal.grid(pady=(10, 0), padx=(20, 0), columnspan=4, row=3, sticky=W)
            else:
                cal.grid(pady=(10, 0), padx=(20, 0), columnspan=7, row=3, sticky=E)

            def set_date(i):
                if i == 0:
                    from_entry.delete(0, END)
                    from_entry.insert(0, cal.get_date())
                    set_from.grid_forget()

                else:
                    to_entry.delete(0, END)
                    to_entry.insert(0, cal.get_date())
                    set_to.grid_forget()
                cal.grid_forget()
                root.geometry('400x300')

            if i == 0:
                set_from.config(command=lambda: set_date(i))
            else:
                set_to.config(command=lambda: set_date(i))

        acnt_no = Label(root, text='Account Number :')
        acnt_no_entry = Entry(root)
        acnt_no.grid(pady=(60, 0), padx=(20, 0), column=1, row=1, sticky=E)
        acnt_no_entry.grid(pady=(60, 0), padx=(20, 0), column=2, row=1, sticky=W)

        period = Label(root, text='Period :')
        period.grid(pady=(10, 0), padx=(20, 0), column=1, row=2, sticky=E)

        from_entry = Entry(root, text='')
        from_entry.grid(pady=(10, 0), row=2, column=2, sticky=E)

        to_entry = Entry(root, text='')
        to_entry.grid(pady=(10, 0), row=2, column=4, padx=(20, 0))

        set_to = Button(root, text='Set', command=lambda: select_date(1))
        set_to.grid(pady=(10, 0), row=2, column=5, padx=(10, 0), sticky=W)

        set_from = Button(root, text='Set', command=lambda: select_date(0))
        set_from.grid(pady=(10, 0), row=2, column=3, padx=(10, 0), sticky=W)

        search_btn = Button(root, text='Search', command=search_transaction)
        search_btn.grid(pady=(30, 0), padx=(20, 0), column=2, row=3, sticky=W)

        root.mainloop()

    @staticmethod
    def deposit_withdraw_money():
        op_type = 0
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

        root = Tk()
        if op_type == 0:
            root.title('Add Money')
        else:
            root.title('Withdraw Money')
        root.geometry('400x300')
        root.minsize(400, 300)
        root.maxsize(600, 400)

        acnt_no = Label(root, text='Account Number :')
        acnt_no.grid(pady=(50, 0), padx=(20, 0), column=1, row=1, sticky=E)
        acnt_no_entry = Entry(root)
        acnt_no_entry.grid(pady=(50, 0), padx=(20, 0), column=2, row=1, sticky=W)

        amount = Label(root, text='Amount :')
        amount.grid(pady=(10, 0), padx=(20, 0), column=1, row=2, sticky=E)
        amount_entry = Entry(root)
        amount_entry.grid(pady=(10, 0), padx=(20, 0), column=2, row=2, sticky=W)

        password = Label(root, text='Password :')
        password.grid(pady=(10, 0), padx=(20, 0), column=1, row=3, sticky=E)
        password_entry = Entry(root)
        password_entry.grid(pady=(10, 0), padx=(20, 0), column=2, row=3, sticky=W)

        add_withdraw_btn = Button(root, text='', command='')
        add_withdraw_btn.grid(pady=(30, 0), padx=(20, 0), columnspan=3, row=4, sticky=E)

        if op_type == 0:
            add_withdraw_btn.config(text='Add Money')
            add_withdraw_btn.config(command=deposit)

        else:
            add_withdraw_btn.config(text='Withdraw')
            add_withdraw_btn.config(command=withdraw)
        root.mainloop()


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """

    # Admin.admin()
    # Admin.admin_control_panel()
    Admin.new_account()
    # Admin.search_transaction_admin()
    # Admin.deposit_withdraw_money()
    # print(ReadWrite.file_writer('test.txt', ReadWrite.pack(['123', 'Uvais', 'A'])))
    # print(ReadWrite.file_writer('test.txt', ReadWrite.pack(['456', 'Test', 'C'])))
    # data = ReadWrite.file_reader('test.txt')
    # for datum in data:
    #     print(ReadWrite.unpack(datum))
