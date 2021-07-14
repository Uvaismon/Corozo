class UniversalData:

    @staticmethod
    def get_next_account_number() -> int:
        """
        :return: Next possible account number.
        """
        return '1'

    @staticmethod
    def get_current_customer_account_file() -> str:
        """
        :return: file name of the latest file to write the customer account details to.
        """
        return 'user.txt'
