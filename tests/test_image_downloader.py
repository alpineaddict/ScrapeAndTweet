"""
Unittest based test framework for functions in app.image_downloader.py
"""

import os
import bs4
import requests
import pytest
import sys
import time
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from requests.exceptions import InvalidURL, Timeout
from app.image_downloader import (
    user_prompt,
    create_repository,
    request_image_search_url,
    create_beautifulsoup_object,
    scrape_image_urls_and_append_to_list,
    download_images,
    delete_zero_byte_images,
)
from tests.samples import SampleData

# CONSTANTS
TEMP_FILEPATH = '/home/ross/AllThingsPython/MyDev/scrape_and_tweet/temp_dir'
IMAGE_SEARCH_ENGINE_URL = 'https://depositphotos.com/stock-photos/'
IMAGE_TO_SEARCH = 'funny pugs'

@patch('app.image_downloader.input', side_effect=[IMAGE_TO_SEARCH, 
        TEMP_FILEPATH])
class TestUserPrompt(TestCase):
    """
    Test image_to_search and filepath input functionality for 
    image_downloader.user_prompt()
    """
    
    def test_user_prompt(self, mock_input):
        prompt_1 = mock_input()
        prompt_2 = mock_input()

        self.assertTrue(prompt_1 == IMAGE_TO_SEARCH)
        self.assertTrue(prompt_2 == TEMP_FILEPATH)

@patch('app.image_downloader.os.chdir')
@patch('app.image_downloader.os.makedirs')
class TestImageRepositoryCreation(TestCase):
    """
    Test image_downloader.create_repository() func, which will also chdir to
    directory. Verify directory was created and is then current working dir.
    Delete directory when finished and verify it was deleted.
    """

    def test_can_create_image_repository(self, mock_mkdir, mock_chdir):
        create_repository(TEMP_FILEPATH)
        self.assertEqual(mock_mkdir.call_count, 1)
        self.assertEqual(mock_chdir.call_count, 1)

    def test_can_create_image_repository_filepath(self, mock_mkdir, mock_chdir):
        create_repository(TEMP_FILEPATH)
        mock_mkdir.assert_called_with(TEMP_FILEPATH, exist_ok=True)
        mock_chdir.assert_called_with(TEMP_FILEPATH)

@patch('app.image_downloader.requests.get')
class TestRequestImageSearchUrl(TestCase):
    """
    Test that request.get() on image search URL is successful. Test exceptions
    as well as status codes for response.
    """

    def setUp(self):
        self.url = IMAGE_SEARCH_ENGINE_URL
        self.img = IMAGE_TO_SEARCH
        self.mock_response = Mock()
        self.mock_response.status_code = 200

    def test_successful_request_status_200(self, mock_request):
        mock_request.return_value = self.mock_response 
        response = request_image_search_url(self.url, self.img)
        self.assertEqual(response.status_code, 200)

    def test_successful_request_attempts_once(self, mock_request):
        mock_request.return_value = self.mock_response
        _response = request_image_search_url(self.url, self.img, attempts=10)
        self.assertEqual(mock_request.call_count, 1)
   
    @patch('app.image_downloader.sys.exit')
    def test_successful_request_status_400(self, _mock_exit, mock_request):
        self.mock_response.status_code = 400
        mock_request.return_value = self.mock_response
        _response = request_image_search_url(self.url, self.img)
        self.assertEqual(_mock_exit.call_count, 1)

    @patch('app.image_downloader.sys.exit')
    def test_successful_request_status_500(self, _mock_exit, mock_request):
        self.mock_response.status_code = 500
        mock_request.return_value = self.mock_response
        _response = request_image_search_url(self.url, self.img)
        self.assertEqual(_mock_exit.call_count, 1)

    def test_invalid_url_exception(self, mock_request):
        mock_request.side_effect = InvalidURL
        with self.assertRaises(SystemExit) as sysexit:
            with self.assertRaises(InvalidURL):
                request_image_search_url(self.url, self.img)
            self.assertTrue(isinstance(sysexit, SystemExit))
    
    def test_timeout_exception(self, mock_request):
        mock_request.side_effect = Timeout
        with self.assertRaises(SystemExit) as sysexit:
            with self.assertRaises(Timeout):
                request_image_search_url(self.url, self.img)
            self.assertTrue(isinstance(sysexit, SystemExit))

class TestBeautifulSoup(TestCase):
    """
    Test that a beautiful soup object is created when passed the response from
    request.get() using the create_beautifulsoup_object() func.
    """

    def test_create_beautifulsoup_object(self):
        response = SampleData()
        soup = create_beautifulsoup_object(response)
        self.assertTrue(isinstance(soup, bs4.BeautifulSoup))

class TestImageScraping(TestCase):
    """
    Test that we can issue find_all method on BeautifulSoup object to extract
    image URLs. Then test that image URLs are being appended to a list.
    """

    def test_image_scrape(self):
        response = SampleData()
        soup = create_beautifulsoup_object(response)
        image_list = scrape_image_urls_and_append_to_list(soup)
        self.assertTrue(isinstance(image_list, list))
        self.assertEqual(response.image_tag, image_list[0])

@patch('app.image_downloader.open')
@patch('app.image_downloader.requests.get')
class TestDownloadImages(TestCase):
    """
    Test that when passed an item from the image list, which is an image URL,
    an image can be successfully downloaded.
    """

    def test_image_download(self, mock_open, mock_request):
        response = SampleData()
        image_list = response.image_list
        download_images(image_list)
        mock_open.assert_called_once()
        mock_request.assert_called_once()

@patch('app.image_downloader.os.remove')
@patch('app.image_downloader.open')
class TestDeleteZeroByteImages(TestCase):
    """
    Test that images of zero bytes in size are deleted if found.
    """
    
    def test_delete_zero_byte_file(self, mock_open, mock_remove):
        with open('zero_byte_file', 'w') as zbf:
            delete_zero_byte_images()

if __name__ == '__main__':
    unittest.main()

