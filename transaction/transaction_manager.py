from datetime import datetime, timedelta, date
from constants import *
from meta import *
from file_handler.read_write import ReadWrite
from file_handler import transaction_indexer
from transaction.secondary_indexer import SecondaryIndexer
from account_manager import *


class TransactionManager:
    """
    This class Handles all transaction details and registers those details in respective transaction data files.
    """

    @staticmethod
    def register_transaction(sender: int, receiver: int, amount: int) -> int:
        """
        Method used to register transaction details.0
        :param sender: Account number of the sender.
        :param receiver: Account number of the receiver.
        :param amount: Amount send to the receiver by sender.
        :return: 0 if transaction is successful, 1 if account doesn't exists and 2 if insufficient balance.
        """
        if receiver != BANK and not customer_account_handler.account_exists(receiver) or\
                sender != BANK and not customer_account_handler.account_exists(sender):
            return 1
        if sender != BANK and customer_account_handler.get_balance(sender) < amount:
            return 2
        date_stamp = datetime.now().date()
        time_stamp = datetime.now().strftime('%H:%M:%S')
        transaction_id = universal_transaction_data.get_next_account_number()
        if universal_transaction_data.get_free_block_size() < 1:
            universal_transaction_data.update_current_account_file()
        file_name = universal_transaction_data.get_current_account_file()
        data_list = [transaction_id, date_stamp, time_stamp, sender, receiver, amount]
        data_list = list(map(str, data_list))
        index = ReadWrite.insert(file_name, TRANSACTION_DATA_DIRECTORY, data_list)
        transaction_indexer.insert_index(1, str(transaction_id), str(index))
        universal_transaction_data.update_next_account_number()
        universal_transaction_data.decrement_free_block_size()

        # Create secondary index
        if not sender == BANK:
            customer_account_handler.update_balance(int(sender), -int(amount))
            SecondaryIndexer.insert_index(str(sender), str(date_stamp), str(transaction_id), WITHDRAW_INDICATOR)
        if not receiver == BANK:
            customer_account_handler.update_balance(int(receiver), int(amount))
            SecondaryIndexer.insert_index(str(receiver), str(date_stamp), str(transaction_id), DEPOSIT_INDICATOR)

    @staticmethod
    def search_transactions(account_number: int, start_date: date, end_date: date,
                            transaction_type: tuple = (DEPOSIT_INDICATOR, WITHDRAW_INDICATOR)) -> list:
        """
        :param transaction_type: Type of transaction, withdrawal or deposit.
        :param account_number: account number of the customer
        :param start_date: starting date of transaction list.
        :param end_date: ending date of transaction list.
        :return: list of transactions.
        """
        dir_path = os.path.join(TRANSACTION_SEC_INDEX_DIRECTORY, str(account_number))
        file_names = [str((start_date + timedelta(days=x))) + '.txt'
                      for x in range((end_date - start_date).days + 1)]

        transactions = []

        for file in file_names:
            transactions += ReadWrite.file_reader(file, dir_path)

        transactions = list(filter(lambda x: x[1] in transaction_type, transactions))
        transaction_records = []

        for transaction in transactions:
            file_name, offset = transaction_indexer.fetch_index(int(transaction[0]))
            data = ReadWrite.file_reader(file_name, TRANSACTION_DATA_DIRECTORY, offset, 1)
            transaction_records += data

        return transaction_records


if __name__ == '__main__':
    """
    Debugging area
    """
    # TransactionManager.search_transactions(1, date(2021, 7, 20), date(2021, 8, 3))
    # TransactionManager.register_transaction(2, 1, 1000)
    print(customer_account_handler.account_exists(1000))
