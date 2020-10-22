from pytest import fixture
from selenium import webdriver
from unittest.mock import patch

@fixture(scope='function')
def test_directory():
    """
    Image repository test directory.
    """
    return "/home/ross/AllThingsPython/MyDev/scrape-and-tweet/test-dir"

@fixture(scope='function')
def search_engine_url():
    """
    Image search engine URL.
    """
    return "https://depositphotos.com/stock-photos/"

@fixture(scope='function')
def image_to_search_for():
    """
    Image to search for within image search engine.
    """
    return "funny pugs"

@fixture(scope='function')
def mock_requests():
    with patch('app.image_downloader.requests'):
        yield




@fixture(scope='function')
def chrome_browser():
    """
    Chrome Selenium browser fixture object.
    """
    return webdriver.Chrome()

@fixture(scope='function')
def firefox_browser():
    """
    Firefox Selenium browser fixture object.
    """
    return webdriver.Firefox()
