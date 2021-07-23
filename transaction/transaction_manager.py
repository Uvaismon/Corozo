from datetime import datetime
from constants import *
from meta import *
from file_handler.read_write import ReadWrite
from file_handler import transaction_index


class TransactionManager:
    """
    This class Handles all transaction details and registers those details in respective transaction data files.
    """

    @staticmethod
    def register_transaction(sender: int, receiver: int, amount: int) -> None:
        """
        Method used to register transaction details.0
        :param sender: Account number of the sender.
        :param receiver: Account number of the receiver.
        :param amount: Amount send to the receiver by sender.
        :return: None
        """
        date_stamp = datetime.now().strftime("%d/%m/%Y")
        time_stamp = datetime.now().strftime("%H:%M:%S")
        transaction_id = universal_transaction_data.get_next_account_number()
        if universal_transaction_data.get_free_block_size() < 1:
            universal_transaction_data.update_current_account_file()
        file_name = universal_transaction_data.get_current_account_file()
        data_list = [transaction_id, date_stamp, time_stamp, sender, receiver, amount]
        data_list = list(map(str, data_list))
        index = ReadWrite.insert(file_name, TRANSACTION_DATA_DIRECTORY, data_list)
        transaction_index.insert_index(1, str(transaction_id), str(index))
        universal_transaction_data.update_next_account_number()
        universal_transaction_data.decrement_free_block_size()


if __name__ == '__main__':
    """
    Debugging area
    """
    TransactionManager.register_transaction(0, 30, 50000)
