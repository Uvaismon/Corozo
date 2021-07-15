import json
import sys

from constants import *

sys.path.append('/...')

customer_meta_file = os.path.join(CUSTOMER_META_DIRECTORY, 'meta.json')
customer_l1_index = os.path.join(CUSTOMER_META_DIRECTORY, '1')
customer_l1_index_file = os.path.join(customer_l1_index, '1.txt')

if __name__ == '__main__':
    """
    Customer index meta initialization
    """
    customer_meta_data = {
        'number_of_levels': 1,
        1: {
            'current_file_number': 1,
            'number_of_entries': 0
        }
    }

    with open(customer_meta_file, 'w') as file:
        json.dump(customer_meta_data, file)

    os.makedirs(customer_l1_index, exist_ok=True)
    with open(customer_l1_index_file, 'w') as file:
        pass
