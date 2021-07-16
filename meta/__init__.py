"""
This package perform handling json files used to store meta data.
"""


from meta.universal_data import UniversalData
from meta.index_data import UserDataIndex
from constants import *

universal_customer_data = UniversalData('customer')
customer_index_meta = UserDataIndex(CUSTOMER_INDEX_META_FILE, CUSTOMER_INDEX_DIRECTORY)

universal_admin_data = UniversalData('admin')
admin_index_meta = UserDataIndex(ADMIN_INDEX_META_FILE, ADMIN_INDEX_DIRECTORY)