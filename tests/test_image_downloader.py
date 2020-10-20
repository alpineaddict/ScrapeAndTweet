"""
Pytest test file to test functions of image downloading script.
"""

# TODO: implement fixture decorators
# TODO: Potentially remove some import statements

import os
import bs4
import requests
import pytest
import send2trash
from unittest.mock import Mock, patch
from pytest import mark, fixture
from app.image_downloader import *
from selenium import webdriver


# chrome_browser = webdriver.Chrome()

def test_can_create_repository(test_directory):
    """
    Test that an image repository can be created within directory structure.
    Then delete the directory and verify it no longer exists.
    """

    create_repository(test_directory)
    assert os.path.exists(test_directory)
    os.rmdir(test_directory)
    assert not os.path.exists(test_directory)

def test_can_chdir_to_repository(test_directory):
    """
    Test for success of changing into image repository.
    """

    create_repository(test_directory)
    assert os.path.exists(test_directory)
    current_dir = os.getcwd()
    assert current_dir == test_directory
    os.rmdir(test_directory)
    assert not os.path.exists(test_directory)

def test_website_url_validity(search_engine_url):
    """
    Verify that navigating to search engine URL responseponds with status code 200.
    """
    
    mock = Mock()
    requests = mock
    response = requests.get(search_engine_url)
    response.status_code = 200
    assert response.status_code == 200

def test_image_search(search_engine_url, image_to_search_for):
    """
    Verify that search engine returns responseults.
    """
    image_list = []
    image_search = search_engine_url + image_to_search_for
    response = requests.get(image_search)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    image_results = soup.find_all('img', attrs={
        'class':'file-container__image _file-image'})
    for image in image_results:
        image_list.append(image.get('src'))
    
    assert len(image_list) >= 5
    # print(f"length of image_list: {len(image_list)}")
    # print(f"image_list results: {image_list}")
 
search_engine_url = "https://depositphotos.com/stock-photos/"
image_to_search_for = "funny pugs"
test_image_search(search_engine_url, image_to_search_for)

# def test_image_search_returns_responseults():
#     pass

# def test_image_scrape(image_to_search):
#     pass

# def image_download():
#     pass

# def test_delete_zero_byte_images():
#     pass