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

    def insert_index(self, level, key, pointer) -> None:
        """
        Registers the index of the given key.
        :param level: Indexing level
        :param key: key for which index has to be build
        :param pointer: offset of the key
        :return:
        """
        new_file = False
        free_block_size = self.user_meta_obj.get_free_block_size(level)
        if not free_block_size:
            self.user_meta_obj.update_current_file(level)
            new_file = True
        file_name = self.user_meta_obj.get_current_file(level)
        if level == 1:
            data_file = universal_customer_data.get_current_account_file()
            data_list = [
                key,
                data_file,
                pointer
            ]
        else:
            data_list = [
                key,
                pointer
            ]

        ReadWrite.insert(file_name, self.__get_level_path(level), data_list)
        self.user_meta_obj.decrement_free_block_size(level)
        if file_name == '2.txt' and new_file:
            self.user_meta_obj.increase_level()
        elif new_file:
            self.get_starting_key(file_name, level)
            self.insert_index(level+1, key, file_name)

    def get_starting_key(self, file_name, level) -> str:
        """
        Returns the first key in a file.
        :param level: Indexing level
        :param file_name: Name of the file to fetch the key from.
        :return: first key of the file
        """
        dir_path = self.__get_level_path(level)
        data = ReadWrite.file_reader(file_name=file_name, dir_path=dir_path, number_or_records=1)[0]
        data_list = ReadWrite.unpack(data)
        return data_list[0]


if __name__ == '__main__':
    """
    Debugging area
    """
