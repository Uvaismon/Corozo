import json
import sys

from constants import *

sys.path.append('/...')


class UserMetaInit:
    """
    Class to initialize user meta file.
    """

    def __init__(self, user):
        if user == 'customer':
            self.l1_index = os.path.join(CUSTOMER_INDEX_DIRECTORY, '1')
            self.l1_index_file = os.path.join(self.l1_index, '1.txt')
            self.meta_file = CUSTOMER_INDEX_META_FILE
            self.initialize()

        if user == 'admin':
            self.l1_index = os.path.join(ADMIN_INDEX_DIRECTORY, '1')
            self.l1_index_file = os.path.join(self.l1_index, '1.txt')
            self.meta_file = ADMIN_INDEX_META_FILE
            self.initialize()

    def initialize(self):
        """
        Customer index meta initialization
        """
        user_meta_data = {
            'number_of_levels': '1',
            '1': INDEX_LEVEL_INIT
        }

        with open(self.meta_file, 'w') as file:
            json.dump(user_meta_data, file)

        os.makedirs(self.l1_index, exist_ok=True)
        with open(self.l1_index_file, 'w') as file:
            pass


if __name__ == '__main__':
    UserMetaInit('customer')
    UserMetaInit('admin')
