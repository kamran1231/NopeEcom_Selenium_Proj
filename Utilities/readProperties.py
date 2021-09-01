

import configparser

config = configparser.RawConfigParser()

config.read("C:/Users/khanb/PycharmProjects/NOPECOM_PROJ/Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicatioURl():
        url = config.get("common info","baseurl")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("common info", "useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password


