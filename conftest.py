import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    # return driver

    yield driver
    # teardown
    print("I am tearing down this browser")


    #yield does not termiate the program whereas return does

