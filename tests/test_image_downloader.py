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
from unittest import mock, TestCase
from unittest.mock import patch
from app.image_downloader import (
    user_prompt,
    create_repository,
    InvalidURL,
    ServerError,
    request_image_search_url,
    create_beautifulsoup_object,
    scrape_image_urls_and_append_to_list,
    download_images,
    delete_zero_byte_images,
)
import urllib3

# CONSTANTS
TEMP_FILEPATH = '/home/ross/AllThingsPython/MyDev/scrape_and_tweet/temp_dir'
IMAGE_SEARCH_ENGINE_URL = 'https://depositphotos.com/stock-photos/'
IMAGE_TO_SEARCH = 'funny pugs'

# class TestUserPrompt(TestCase):
#     """
#     Test image_to_search and filepath input functionality for 
#     image_downloader.user_prompt()
#     """
    
#     @patch('builtins.input', side_effect=[IMAGE_TO_SEARCH, TEMP_FILEPATH])
#     def test_user_prompt(self, mock_input):
#         prompt_1 = mock_input()
#         prompt_2 = mock_input()

#         self.assertTrue(prompt_1 == IMAGE_TO_SEARCH)
#         self.assertTrue(prompt_2 == TEMP_FILEPATH)

# class TestImageRepositoryCreation(TestCase):
#     """
#     Test image_downloader.create_repository() func, which will also chdir to
#     directory. Verify directory was created and is then current working dir.
#     Delete directory when finished and verify it was deleted.
#     """

#     def setUp(self):
#         pass

#     def tearDown(self):
#         os.chdir('..')
#         os.rmdir(TEMP_FILEPATH)
#         self.assertNotIn(TEMP_FILEPATH, os.listdir())

#     def test_can_create_image_repository(self):
#         create_repository(TEMP_FILEPATH)
#         self.assertEqual(os.getcwd(), TEMP_FILEPATH)


@patch('.app.image_downloader.request_image_search_url.requests.get')
class TestRequestImageSearchURL(TestCase):
    """
    Test that request.get() on image search URL is successful and that 
    raise_for_response does not return an error. None means success. Test
    exceptions behave as expected.
    """

    def setUp(self):
        self.url = IMAGE_SEARCH_ENGINE_URL
        self.img = IMAGE_TO_SEARCH

    def test_response_from_request_is_200(self):
        # mock_request.status_code = 200
        response = request_image_search_url(self.url, self.img)
        self.assertEqual(response.status_code, 200)
        # self.assertEquals(mock_request.call_count, 1)


    # def test_missing_schema_exception(self):
    #     self.assertRaises(request_image_search_url
    #         MissingSchema,
    #         request_image_search_url,
    #         'not an actual URL',
    #         IMAGE_TO_SEARCH,
    #         0
    #     )

    # def test_invalid_url_exception(self):
    #     self.assertRaises(
    #         InvalidURL,
    #         request_image_search_url,
    #         'https://notworking.url/',
    #         IMAGE_TO_SEARCH,
    #         0
    #     )
        

    # def test_timeout_exception(self):
    #     pass

# class BeautifulSoupTest(TestCase):
#     """
#     Test that a beautiul soup object is created when passed the response from
#     request.get() using the create_beautifulsoup_object() func.
#     """

#     def test_create_beautifulsoup_object(self):
#         soup = create_beautifulsoup_object(request_image_search_url(
#             IMAGE_SEARCH_ENGINE_URL, IMAGE_TO_SEARCH))
#         self.assertTrue(isinstance(soup, bs4.BeautifulSoup))


if __name__ == '__main__':
    unittest.main()

