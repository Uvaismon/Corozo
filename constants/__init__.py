"""
This package stores all app constants
"""

import logging
import os

logging.basicConfig(filename='log.txt', level=logging.DEBUG)


DATA_DIRECTORY = os.path.join(r'D:\Python\Corozo', 'app_data')
META_DIRECTORY = os.path.join(DATA_DIRECTORY, 'meta')

CUSTOMER_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'customer_data', 'data')
CUSTOMER_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'customer_data', 'index')
CUSTOMER_INDEX_META_FILE = os.path.join(CUSTOMER_INDEX_DIRECTORY, 'meta.json')

ADMIN_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'admin_data', 'data')
ADMIN_INDEX_DIRECTORY = os.path.join(DATA_DIRECTORY, 'admin_data', 'index')
ADMIN_INDEX_META_FILE = os.path.join(ADMIN_INDEX_DIRECTORY, 'meta.json')

BLOCK_SIZE = 3
MAX_DIGITS = 9
PASSWORD_SIZE = 10

INDEX_LEVEL_INIT = {
    "current_file_number": "1",
    "number_of_entries": "0"
}
