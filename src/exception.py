import sys

def error_message_detail(error, error_detail: sys):
    # This line has 4 spaces of indentation
    _, _, exc_tb = error_detail.exc_info()
    
    # Indent this line by 4 spaces too!
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Indent this line by 4 spaces too!
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    # Indent this line by 4 spaces so Python knows it belongs to the function!
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message