import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common Info', 'baseurl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common Info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common Info', 'password')
        return password


