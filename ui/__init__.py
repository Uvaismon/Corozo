"""
This package contains frontend implementation of the app.
"""
from tkinter import Tk, Label, ttk


def account_statement(transaction_list: list, account_number: int, customer_name: str):
    """
    Frame ID: 007
    This method renders the window that displays the users account statement.
    It takes in the following arguments
    transaction list -> list of transactions
    """
    root = Tk()
    root.title('Transaction details.')
    root.maxsize(630, 580)
    root.minsize(630, 580)
    account_number_label = Label(root, text=f'Account number: {account_number}')
    account_number_label.place(x=20, y=20)
    account_number_label = Label(root, text=f'Customer name: {customer_name}')
    account_number_label.place(x=300, y=20)
    tree_view = ttk.Treeview(root, show='headings', height=25)
    tree_view.place(x=20, y=50)
    tree_view['columns'] = ('1', '2', '3', '4', '5', '6')
    tree_view.column('1', width=100, anchor='c')
    tree_view.column('2', width=100, anchor='c')
    tree_view.column('3', width=100, anchor='c')
    tree_view.column('4', width=100, anchor='c')
    tree_view.column('5', width=100, anchor='c')
    tree_view.column('6', width=100, anchor='c')
    tree_view.heading('1', text='ID')
    tree_view.heading('2', text='Date')
    tree_view.heading('3', text='Time')
    tree_view.heading('4', text='Sender')
    tree_view.heading('5', text='Receiver')
    tree_view.heading('6', text='Amount')

    for transaction in transaction_list:
        tree_view.insert('', 'end',
                         values=transaction)

    root.mainloop()
