
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


############Pytest Html Report############

#it is hook for adding enviroment info to Html Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'kamran'


#it is hook for delete/modify enviroment info to Html Report

@pytest.mark.optionalhook
def pytest_matadata(metadata):
    metadata.pop('Java_Home',None)
    metadata.pop('Plugins',None)