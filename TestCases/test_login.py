
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseurl = ReadConfig.getApplicatioURl()

    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()


    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title


        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:/Users/khanb/PycharmProjects"
                                        "/NOPECOM_PROJ/Screenshots"+"/test_homePageTitle_error.jpg")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup

        self.driver.get(self.baseurl)

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title


        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:/Users/khanb/PycharmProjects/"
                                        "NOPECOM_PROJ/Screenshots"+"/test_login_error.jpg")
            self.driver.close()
            assert False


if __name__ == '__main__':
    pytest.main()