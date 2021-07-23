import os
from constants import *
from file_handler.read_write import ReadWrite


class SecondaryIndexer:

    @staticmethod
    def insert_index(account_number: str, date: str, transaction_id: str, transaction_type: int) -> None:
        """
        Insert new index to secondary index files.
        :param account_number: account number of the customer involved
        :param date: date of the transaction
        :param transaction_id: transaction ID referring to the key in transaction records.
        :param transaction_type: Type of the transaction, 0 for deposit, 1 for withdrawal.
        :return: None
        """
        dir_path = os.path.join(TRANSACTION_SEC_INDEX_DIRECTORY, account_number)
        os.makedirs(dir_path, exist_ok=True)
        date = date.replace('/', '-')
        file_name = f'{date}.txt'
        ReadWrite.insert(file_name, dir_path, [transaction_id, transaction_type])
