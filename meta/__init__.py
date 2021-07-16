"""
This package perform handling json files used to store meta data.
"""


from meta.universal_data import UniversalData
from meta.index_data import UserDataIndex
from constants import *

universal_customer_data = UniversalData('customer')
customer_index_meta = UserDataIndex(CUSTOMER_INDEX_META_FILE)
