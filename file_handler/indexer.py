from meta import *
from file_handler.read_write import ReadWrite


class Indexer:

    def __init__(self, user):
        """
        Initializes the class according to the user.
        :param user: customer or admin
        :return: None
        """
        if user == 'customer':
            self.user_meta_obj = customer_index_meta
            self.dir_path = CUSTOMER_INDEX_DIRECTORY

        if user == 'admin':
            self.user_meta_obj = admin_index_meta
            self.dir_path = ADMIN_INDEX_DIRECTORY

    def __get_level_path(self, level) -> str:
        """
        :param level: Index level
        :return: Path to the given level.
        """
        return os.path.join(self.dir_path, str(level))

    def insert_l1_index(self, key, offset) -> None:
        """
        Registers the level 1 index of the given key.
        :param key: key for which index has to be build
        :param offset: offset of the key
        :return:
        """
        free_block_size = self.user_meta_obj.get_free_block_size(1)
        if not free_block_size:
            self.user_meta_obj.update_current_file(1)
        data_file = universal_customer_data.get_current_account_file()
        file_name = self.user_meta_obj.get_current_file(1)
        ReadWrite.insert(file_name,
                         self.__get_level_path(1),
                         [
                             key,
                             data_file,
                             offset
                         ])
        self.user_meta_obj.decrement_free_block_size(1)
