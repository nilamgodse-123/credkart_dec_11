import logging

class log_generator_class:

    @staticmethod
    def loggen_method():
        logger = logging.getLogger() # called the logger method to create the log
        log_file = logging.FileHandler(".\\Logs\\CredKart_Automation.log") # here er have given log file's path
        # log_file = logging.FileHandler(r"C:\PycharmBasic\folder\Credkart_login_testcases\TestData\Test_Data.xlsx")
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d -  %(message)s') # here  have given log format
        log_file.setFormatter(log_format) # here have set the log format
        logger.addHandler(log_file) # here have added log file to logger
        logger.setLevel(logging.INFO) # here have set the log level
        return logger


# Debug
# info
# warning
# error
# critical