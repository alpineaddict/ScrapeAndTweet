from pytest import fixture
from selenium import webdriver

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture(scope='function')
def firefox_browser():
    browser = webdriver.Firefox()
    return browser

    