
import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",format="%(asctime)s: %(levelname)s: "
                                                                                "%(name)s: %(message)s",
                            datefmt='%m-%d-%y %I:%M:%S')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger