"""
This package stores all app constants
"""

import logging
import os


DATA_DIRECTORY = os.path.join(os.environ.get('PYTHONPATH'), 'app_data')
META_DIRECTORY = os.path.join(DATA_DIRECTORY, 'meta')

CUSTOMER_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'customer_data', 'data')
CUSTOMER_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'customer_data', 'index')
CUSTOMER_INDEX_META_FILE = os.path.join(CUSTOMER_INDEX_DIRECTORY, 'meta.json')

ADMIN_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'admin_data', 'data')
ADMIN_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'admin_data', 'index')
ADMIN_INDEX_META_FILE = os.path.join(ADMIN_INDEX_DIRECTORY, 'meta.json')

TRANSACTION_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'transaction_data', 'data')
TRANSACTION_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'transaction_data', 'index')
TRANSACTION_INDEX_META_FILE = os.path.join(TRANSACTION_INDEX_DIRECTORY, 'meta.json')
TRANSACTION_SEC_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'transaction_data', 'sec_index')

LOG_FILE = os.path.join(META_DIRECTORY, 'log.ini')

# with open(LOG_FILE, 'a') as _:
#     pass
# logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

BLOCK_SIZE = 3
MAX_DIGITS = 9
PASSWORD_SIZE = 10

DEPOSIT_INDICATOR = "0"
WITHDRAW_INDICATOR = "1"

INDEX_LEVEL_INIT = {
    "current_file_number": "1",
    "number_of_entries": "0"
}
