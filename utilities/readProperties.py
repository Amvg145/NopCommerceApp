import configparser

config = configparser.RawConfigParser()
configarationPath = 'D:\\NopCommerceApp\\Configurations\\config.ini'
config.read(configarationPath)

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        userName = config.get('info', 'userName')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('info', 'password')
        return password

    @staticmethod
    def getScreenshotPath():
        ScreenShot_path = config.get('info', 'screenshot_path')
        return ScreenShot_path

