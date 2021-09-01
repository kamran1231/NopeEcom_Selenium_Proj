
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicatioURl()

    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info('*************Test_001_Login*************')
        self.logger.info('*************Verifying Home page title*************')
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title


        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info('*************Homepage title test is passed*************')

        else:
            self.driver.save_screenshot("C:/Users/khanb/PycharmProjects"
                                        "/NOPECOM_PROJ/Screenshots"+"/test_homePageTitle_error.jpg")
            self.driver.close()
            self.logger.error('*************Home page title is failed*************')

            assert False

    def test_login(self,setup):
        self.logger.info('*************Verifying login Test*************')

        self.driver = setup

        self.driver.get(self.baseurl)

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title


        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info('*************Login Test is passed*************')

            self.driver.close()
        else:
            self.driver.save_screenshot("C:/Users/khanb/PycharmProjects/"
                                        "NOPECOM_PROJ/Screenshots"+"/test_login_error.jpg")
            self.driver.close()
            self.logger.error('*************Login Test is failed*************')

            assert False


if __name__ == '__main__':
    pytest.main()