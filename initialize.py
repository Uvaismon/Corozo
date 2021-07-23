import os
from constants import *
from meta import universal_data, user_init

# Initialize file structure and meta files.

os.makedirs(DATA_DIRECTORY, exist_ok=True)
os.makedirs(ADMIN_DATA_DIRECTORY, exist_ok=True)
os.makedirs(CUSTOMER_DATA_DIRECTORY, exist_ok=True)
os.makedirs(ADMIN_INDEX_DIRECTORY, exist_ok=True)
os.makedirs(CUSTOMER_INDEX_DIRECTORY, exist_ok=True)
os.makedirs(TRANSACTION_DATA_DIRECTORY, exist_ok=True)
os.makedirs(TRANSACTION_INDEX_DIRECTORY, exist_ok=True)
os.makedirs(META_DIRECTORY, exist_ok=True)
os.makedirs(TRANSACTION_SEC_INDEX_DIRECTORY, exist_ok=True)

# universal_data.initialize()
# user_init.initialize()

