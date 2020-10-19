"""
Pytest test file to test functions of image downloading script.
"""

# TODO: implement fixture decorators

import os
import bs4
import requests
import unittest
import pytest
from unittest.mock import Mock, patch
from pytest import mark

from app.image_downloader import user_prompt

def test_can_create_repository():
    test_path = '/home/ross/AllThingsPython/MyDev/scrape-and-tweet/test-dir'
    create_repository(test_path)
    assert os.path.exists(test_path)
    os.rmdir(test_path)
    assert not os.path.exists(test_path)

@patch('os.chdir')
def test_can_chdir_to_repository(mock_chdir):
    test_path = '/home/ross/AllThingsPython/MyDev/scrape-and-tweet/test-dir'
    create_repository(test_path)
    assert os.path.exists(test_path)
    assert mock_chdir.called
    os.rmdir(test_path)
    assert not os.path.exists(test_path)

def test_can_navigate_to_photo_search_page_in_chrome(chrome_browser):
    search_engine_url = 'https://depositphotos.com/stock-photos/'
    chrome_browser.get(search_engine_url)
    assert True

def test_can_navigate_to_photo_search_page_in_firefox(firefox_browser):
    search_engine_url = 'https://depositphotos.com/stock-photos/'
    firefox_browser.get(search_engine_url)
    assert True

# def test_image_search_returns_results():
#     pass

# def test_image_scrape(image_to_search):
#     pass

# def image_download():
#     pass

# def test_delete_zero_byte_images():
#     pass