import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="C:\\Users\\Master\\PycharmProjects\\nonCommerceApp\\Logs\\"+"test_login.log", mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
