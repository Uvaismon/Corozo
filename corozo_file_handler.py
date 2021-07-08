class CorozoFileHandler:

    def __init__(self):
        pass

    def file_writer(self, file_name: str, data: int, byte_loc=None) -> int:
        """
        This function performs all operations of writing data to any file.
        It takes 3 arguments of which 1 is a default argument.
        file_name -> the name of the file to which the function should write.
        data -> data to be written to the file.
        byte_loc -> offset where the data should be written. If byte_loc is not passed, it appends the data to the end
            of the file.
        Return 0 if writing is successful, 1 otherwise.
        """
        pass

    def file_reader(self, file_name: str, offset=0, number_or_records=None) -> list[str]:
        """
        This function performs all the operations of reading data from the file.
        It takes 3 arguments of which 1 is a default argument.
        file_name -> Name of the file to be read from.
        offset -> byte location from which the function should read data. If this is not passed, the function reads
            from the beginning.
        number_of_records -> number of records to be read. If this argument is not passed, the function reads till the
            end of the file.
        Returns the data read as a list of records.
        """
        pass

    def pack(self, data_list: list) -> str:
        """
        This function is used to construct field structure. It can take in a list of data and return a string after
        transforming the list of data into str of fields.
        """
        pass

    def unpack(self, data_string) -> list:
        """
        This function can take in a string of fields and return a list of individual fields after unpacking it.
        """
        pass

