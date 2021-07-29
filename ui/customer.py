from tkinter import *
from tkcalendar import *
from account_manager import customer_account_handler, UserAccountFileHandler
from ui.admin import Admin
from tkinter import messagebox
from transaction.transaction_manager import TransactionManager
from constants import *
from datetime import date
from ui import account_statement


class Customer:
    logged_in_customer = None
    logged_in_name = None
    logged_in_type = None

    @staticmethod
    def error_message(message):
        messagebox.showerror('Error', message)

    @staticmethod
    def warning_message(message):
        messagebox.showwarning('Warning', message)

    @staticmethod
    def info_message(message):
        messagebox.showinfo('Info', message)

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
            entered_password = e2.get()
            entered_account = int(e.get())
            auth = customer_account_handler.authenticate(entered_account, entered_password)
            if auth:
                root.destroy()
                Customer.logged_in_customer = auth['account_number']
                Customer.logged_in_name = auth['account_holder_name']
                Customer.logged_in_type = auth['account_type']
                Customer.home()
            else:
                # Display authentication failed message.
                message = 'Authentication failed'
                Customer.error_message(message)
                return

        def admin():
            root.destroy()
            Admin.admin()

        def validate_act_no():
            try:
                int(e.get())
                log_in()
            except ValueError:
                message = "Account number must be numeric"
                Customer.error_message(message)

        root = Tk()
        root.title('Log In')
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)
        root.title("Login")

        account_number = Label(root, text="Enter Account Number")

        e = Entry(root, width=30)

        passcode = Label(root, text="Enter Passcode: ")
        e2 = Entry(root, width=30)

        account_number.grid(row=1, column=0)
        e.grid(row=1, column=1, padx=10, pady=10)

        passcode.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        my_button = Button(root, text="Login", command=validate_act_no)
        my_button.grid(row=3, column=1)
        # welcome.grid(row=0, column=0)

        admin_button = Button(root, text="ADMIN", command=admin)
        admin_button.grid(row=4, column=3)

        root.mainloop()

    @staticmethod
    def home():
        """
        Frame ID: 002
        This method renders the home window.
        The window provides 2 choices to the users.
        The method calls transaction handler if user clicks transact button and settings handler
            if user clicks settings button.
        """

        def transact():
            root.destroy()
            Customer.transact()

        def settings():
            root.destroy()
            Customer.settings()

        root = Tk()
        root.title('Home')
        root.geometry("400x400")
        root.minsize(400, 400)
        root.maxsize(400, 400)
        root.title("Home")

        account_number = Label(root, text="Account Number")

        e1 = Label(root, text=Customer.logged_in_customer, width=30)

        account_holder_name = Label(root, text="Account holder name: ")
        e2 = Label(root, text=Customer.logged_in_name, width=30)

        account_number.grid(row=1, column=0, sticky='W', padx=10)
        e1.grid(row=1, column=1, padx=10, pady=10)

        account_holder_name.grid(row=2, column=0, sticky='W', padx=10)
        e2.grid(row=2, column=1, padx=10, pady=10)

        account_type = Label(root, text="Account transaction_type")

        e3 = Label(root, text=Customer.logged_in_type, width=30)

        account_balance = Label(root, text="The balance is: ")
        e4 = Label(root, text=customer_account_handler.get_balance(Customer.logged_in_customer), width=30)

        account_type.grid(row=3, column=0, sticky='W', padx=10)
        e3.grid(row=3, column=1, padx=10, pady=10)

        account_balance.grid(row=4, column=0, sticky='W', padx=10)
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
            root.destroy()
            Customer.change_password()

        def close_account_window():
            root.destroy()
            Customer.close_account()

        root = Tk()
        root.title('Settings')
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)

        change_password = Button(root, text="Change Password", command=change_password_window)
        change_password.grid(row=1, column=0, padx=20, pady=15)

        close_account = Button(root, text="Close Account", command=close_account_window)
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

        def account_statement_window():
            account_statement(TransactionManager.fetch_account_statement(Customer.logged_in_customer),
                              Customer.logged_in_customer, Customer.logged_in_name,
                              customer_account_handler.get_balance(Customer.logged_in_customer))

        def search_transaction_window():
            Customer.search_transactions()

        def send_money_window():
            root.destroy()
            Customer.send_money()

        root = Tk()
        root.title('Transact')
        root.geometry("400x400")
        root.minsize(400, 200)
        root.maxsize(400, 200)

        account_statement_button = Button(root, text="Account Statement", command=account_statement_window)
        account_statement_button.grid(row=1, column=0, padx=20, pady=15)

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
            old_password = e.get()
            new_password = e2.get()
            re_entered_password = e3.get()
            if len(new_password)<11:
                if len(new_password)> 5:
                    strength = UserAccountFileHandler.pass_strength(new_password)
                else:
                    message = 'Password length should be greater than 6 characters and less than 10 characters.'
                    Customer.info_message(message)
                    return
            else:
                message='Password length should be greater than 6 characters and less than 10 characters.'
                Customer.info_message(message)
                return

            authenticated = customer_account_handler.authenticate(Customer.logged_in_customer, old_password)

            if not authenticated:
                # Display authentication failed message
                message = 'Authentication failed'
                Customer.error_message(message)
                return

            if not new_password == re_entered_password:
                # Display password does not match errors.
                message = 'Password does not match'
                Customer.warning_message(message)
                return

            if not strength:
                # Display new password not strong enough error.
                message = 'Password not strong enough'
                Customer.warning_message(message)
                return

            message='Password changed'
            Customer.info_message(message)
            root.destroy()
            customer_account_handler.change_password(Customer.logged_in_customer, new_password)
            Customer.log_in()

        root = Tk()
        root.title('Change password')
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
    def close_account():
        """
        Frame ID: 006
        This method renders the close account window. It takes in the following arguments.
        account number -> int,
        account balance -> float
        This method calls close account manager if user chooses to close account:
        """
        balance = customer_account_handler.get_balance(Customer.logged_in_customer)

        def delete_account():
            entered_password = e3.get()
            if customer_account_handler.authenticate(Customer.logged_in_customer, entered_password):

                # Display account closed successfully message.
                message = 'Account closed successfully'
                Customer.info_message(message)

                root.destroy()
                customer_account_handler.delete_account(Customer.logged_in_customer)
                Customer.log_in()
            else:
                # Display authentication failed message
                message = 'Authentication failed'
                Customer.warning_message(message)

        root = Tk()
        root.title('Close account')

        account_number = Label(root, text="Account Number")

        e1 = Label(root, text=Customer.logged_in_customer, width=30)

        account_balance = Label(root, text="Account Balance is : ")
        e2 = Label(root, text=balance, width=30)

        password = Label(root, text="Enter Password")
        e3 = Entry(root, width=30)

        account_number.grid(row=1, column=0)
        e1.grid(row=1, column=1, padx=10, pady=10)

        account_balance.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        password.grid(row=3, column=0)
        e3.grid(row=3, column=1, padx=10, pady=10)

        close_account_button = Button(root, text="Close", command=delete_account)
        close_account_button.grid(row=4, column=0, padx=30, pady=15)

        root.mainloop()

    @staticmethod
    def search_transactions():
        """
        Frame ID: 008
        This method renders the window that displays that lets users filter their transactions based on time
        period and transaction_type of transaction.
        This method calls transaction filtering window.
        """

        def filter_transaction():
            start_month, start_date, start_year = list(map(int, from_entry.get().split('/')))
            end_month, end_date, end_year = list(map(int, to_entry.get().split('/')))
            start_year += 2000
            end_year += 2000
            start = date(start_year, start_month, start_date)
            end = date(end_year, end_month, end_date)
            t_type = tuple(items.get())
            root.destroy()

            account_statement(TransactionManager.search_transactions(Customer.logged_in_customer, start, end, t_type),
                              Customer.logged_in_customer,
                              customer_account_handler.get_user_name(Customer.logged_in_customer),
                              customer_account_handler.get_balance(Customer.logged_in_customer))

        root = Tk()
        root.title("Search Transaction")
        root.geometry("500x300")
        root.minsize(600, 400)
        root.maxsize(600, 400)

        def select_date(cal_pos):
            root.geometry('600x400')
            cal = Calendar(root, selectmode='day', year=2021, month=7, day=15)
            if cal_pos == 0:
                cal.grid(pady=(10, 0), padx=(20, 0), columnspan=4, row=3, sticky=W)
            else:
                cal.grid(pady=(10, 0), padx=(20, 0), columnspan=7, row=3, sticky=E)

            def set_date(entry_box):
                if entry_box == 0:
                    from_entry.delete(0, END)
                    from_entry.insert(0, cal.get_date())
                    set_from.grid_forget()

                else:
                    to_entry.delete(0, END)
                    to_entry.insert(0, cal.get_date())
                    set_to.grid_forget()
                cal.grid_forget()
                root.geometry('400x300')

            if cal_pos == 0:
                set_from.config(command=lambda: set_date(cal_pos))
            else:
                set_to.config(command=lambda: set_date(cal_pos))

        by_date = Label(root, text='By Date :')
        by_date.grid(pady=(5, 0), padx=(20, 0), row=2, column=1, sticky=E)

        from_label = Label(root, text='From')
        to_label = Label(root, text="To")
        from_label.grid(pady=(50, 0), row=1, column=2, sticky=W)
        to_label.grid(pady=(50, 0), row=1, column=4, padx=(20, 0), sticky=W)

        from_entry = Entry(root, text='')
        from_entry.grid(pady=(5, 0), row=2, column=2)

        to_entry = Entry(root, text='')
        to_entry.grid(pady=(5, 0), row=2, column=4, padx=(20, 0))

        set_to = Button(root, text='Set', command=lambda: select_date(1))
        set_to.grid(pady=(5, 0), row=2, column=5, padx=(10, 0), sticky=W)

        set_from = Button(root, text='Set', command=lambda: select_date(0))
        set_from.grid(pady=(5, 0), row=2, column=3, padx=(10, 0), sticky=W)

        transaction_type = Label(root, text='Transaction type :')
        transaction_type.grid(pady=(20, 0), padx=(20, 0), sticky=E, row=4, column=1)

        items = StringVar(root, '1')
        values = {
            "Credited": DEPOSIT_INDICATOR,
            "Debited": WITHDRAW_INDICATOR,
            "Both": (DEPOSIT_INDICATOR, WITHDRAW_INDICATOR)
        }
        i = 2
        for (text, value) in values.items():
            Radiobutton(root, text=text, variable=items, value=value).grid(pady=(20, 0), padx=(20, 0), column=i, row=4,
                                                                           sticky=E)
            i = i + 2
        search = Button(root, text="Search", command=filter_transaction)
        search.grid(columnspan=7, pady=(30, 0), padx=(30, 0))
        root.mainloop()

    @staticmethod
    def send_money():
        """
        Frame ID: 009
        This method renders the window that lets users send money to another account.
        This method calls money sending handler.
        """

        def send_money():
            receiver = int(e1.get())
            entered_amount = int(e2.get())
            transaction_status = TransactionManager.register_transaction(Customer.logged_in_customer, receiver,
                                                                         entered_amount)
            if transaction_status == 1:
                Customer.error_message('Account number does not exists.')
                return
            if transaction_status == 2:
                Customer.warning_message('Insufficient balance')
                return
            if transaction_status == 3:
                Customer.error_message('Cannot perform self transfer.')
                return
            Customer.info_message('Money sent successfully.')
            root.destroy()
            Customer.home()

        root = Tk()
        root.title('Send money')

        def validate_amount():
            try:
                int(e2.get())
                send_money()
            except ValueError:
                message = "Amount must be numeric"
                Customer.error_message(message)

        def validate_act_no():
            try:
                int(e1.get())
                validate_amount()
            except ValueError:
                message = "Account number must be numeric"
                Customer.error_message(message)

        account_number = Label(root, text="Enter Account Number")
        e1 = Entry(root, width=30)

        amount = Label(root, text="Enter Amount")
        e2 = Entry(root, width=30)

        account_number.grid(row=1, column=0)
        e1.grid(row=1, column=1, padx=10, pady=10)

        amount.grid(row=2, column=0)
        e2.grid(row=2, column=1, padx=10, pady=10)

        send = Button(root, text="Send", command=validate_act_no)
        send.grid(row=3, column=0, padx=10, pady=10)

        root.mainloop()


if __name__ == '__main__':
    """
    If you have to debug and test any of the CorozoUI class methods, please do it in this block.
    """

    Customer.log_in()
    # Customer.home(1234, "zabi", "Savings", 5000)
    # Customer.settings()
    # Customer.transact()
    # Customer.change_password()
    # Customer.close_account()
    # Customer.send_money()
    # Customer.search_transactions()
