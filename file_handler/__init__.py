"""
This package performs all file handling tasks.
"""

from file_handler.indexer import Indexer
from file_handler.read_write import ReadWrite

customer_indexer = Indexer("customer")
admin_indexer = Indexer('admin')
transaction_indexer = Indexer('transactor')
