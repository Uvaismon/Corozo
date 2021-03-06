import os
from constants import *

FIELD_SEPARATOR = '|'
RECORD_SEPARATOR = '\n'
DELETION_INDICATOR = '#'


class ReadWrite:

    @staticmethod
    def file_writer(file_name: str, dir_path: str, data: str, offset: int = None) -> int:
        """
        This function performs all operations of writing data to any file.
        It takes 2 arguments of which 1 is a default argument.
        file_name -> the name of the file to which the function should write.
        data -> data to be written to the file.
        dir_path -> directory path where the file is located.
        offset -> offset from where the data need to be written.
        Returns byte pointer of the record written to the file.
        """
        file = None
        sep_req = True
        file_path = os.path.join(dir_path, file_name)
        try:
            file = open(file_path, 'r+')
            if offset is None:
                file.seek(0, 2)
            else:
                file.seek(offset)
                sep_req = False
            offset = file.tell()
            file.write(data)
            if sep_req:
                file.write(RECORD_SEPARATOR)
            return offset

        except FileNotFoundError:
            file =  open(file_path, 'w')
            return ReadWrite.file_writer(file_name, dir_path, data, offset)

        finally:
            if file:
                file.close()



    @staticmethod
    def file_reader(file_name: str, dir_path: str, offset=0, number_or_records: int = None) -> list:
        """
        This function performs all the operations of reading data from the file.
        It takes 3 arguments of which 1 is a default argument.
        file_name -> Name of the file to be read from.
        pointer -> byte location from which the function should read data. If this is not passed, the function reads
            from the beginning.
        number_of_records -> number of records to be read. If this argument is not passed, the function reads till the
            end of the file.
        dir_path -> directory path where the file is located.
        Returns the data read as a list of strings, empty list if the read fails
        """
        file_path = os.path.join(dir_path, file_name)
        file = None
        try:
            file = open(file_path)
            file.seek(offset)
            lines = []
            if not number_or_records:
                data_lines = file.readlines()
                for line in data_lines:
                    if line[0] == DELETION_INDICATOR:
                        continue
                    lines.append(line)
                return list(map(ReadWrite.unpack, lines))
            for _ in range(number_or_records):
                line = file.readline()
                if line[0] == DELETION_INDICATOR:
                    continue
                lines.append(line)
            return list(map(ReadWrite.unpack, lines))

        except FileNotFoundError:
            return []

        finally:
            if file:
                file.close()

    @staticmethod
    def pack(data_list: list) -> str:
        """
        This function is used to construct field structure. It can take in a list of data and return a string after
        transforming the list of data into str of fields.
        """
        return FIELD_SEPARATOR.join(data_list)

    @staticmethod
    def unpack(data_string: str) -> list:
        """
        This function can take in a string of fields and return a list of individual fields after unpacking it.
        """
        data_string = data_string.replace(RECORD_SEPARATOR, '')
        return data_string.split(FIELD_SEPARATOR)

    @staticmethod
    def insert(file_name: str, dir_path: str, data: list) -> int:
        """
        This method takes in a list of fields and add the record to the file.
        :param dir_path: directory at which the file exists.
        :param file_name: Name of the file to insert data.
        :param data: record fields are list.
        :return: byte pointer of the beginning of the record.
        """
        data_string = ReadWrite.pack(data)
        return ReadWrite.file_writer(file_name, dir_path, data_string)


if __name__ == "__main__":
    """
    Debugging block
    """
    # print(ReadWrite.file_writer('test.txt', ReadWrite.pack(['123', 'Uvais', 'A'])))
    # print(ReadWrite.file_writer('test.txt', ReadWrite.pack(['456', 'Test', 'C'])))
    # data = ReadWrite.file_reader('test.txt')
    # for datum in data:
    #     print(ReadWrite.unpack(datum))
