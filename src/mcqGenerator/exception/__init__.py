import sys


def error_message_detail(error, error_detail: sys):
    """
    Method Name : error_message_detail
    Description : Format and return an error message with traceback details.
    Return : str
    Args  :
        error (Exception): The error object or message.
        error_detail (sys): The traceback information from the error.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] at line number [{1}]. Error message: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class MoneyLaunderingException(Exception):
    """
    Custom exception class for handling money laundering-related errors.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Method Name : __init__
        Description : Initialize the MoneyLaunderingException exception.
        Return : None
        Args  :
            error_message (str): The main error message.
            error_detail (sys): Additional details about the error.
        """
        super().__init__(error_message)
        self.error_message_detail = error_detail

    def __str__(self):
        """
        Method Name : __str__
        Description : Return a string representation of the MoneyLaundering exception.
        Return : str
        Args  : None
        """
        return str(self.error_message_detail)