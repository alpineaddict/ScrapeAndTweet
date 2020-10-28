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

    # def test_successful_request_attempts_once(self, mock_request):
    #     mock_request.return_value = self.mock_response
    #     _response = request_image_search_url(self.url, self.img, attempts=10)
    #     self.assertEqual(mock_request.call_count, 1)
   
    # @patch('app.image_downloader.sys.exit')
    # def test_successful_request_status_400(self, _mock_exit, mock_request):
    #     self.mock_response.status_code = 400
    #     mock_request.return_value = self.mock_response
    #     _response = request_image_search_url(self.url, self.img)
    #     self.assertEqual(_mock_exit.call_count, 1)

    # @patch('app.image_downloader.sys.exit')
    # def test_successful_request_status_500(self, _mock_exit, mock_request):
    #     self.mock_response.status_code = 500
    #     mock_request.return_value = self.mock_response
    #     _response = request_image_search_url(self.url, self.img)
    #     self.assertEqual(_mock_exit.call_count, 1)

    # @patch('app.image_downloader.sys.exit')
    # def test_invalid_url_exception(self, _mock_exit, mock_request):
    #     mock_request.side_effect = [InvalidURL("wrong URL")]
    #     with self.assertRaises(InvalidURL):
    #         request_image_search_url(self.url, self.img)

    # def test_invalid_url_exception(self, mock_request):
    #     mock_request.side_effect = InvalidURL
    #     with self.assertRaises(SystemExit) as sysexit:
    #         with self.assertRaises(InvalidURL):
    #             request_image_search_url(self.url, self.img)
    #         self.assertTrue(isinstance(sysexit, SystemExit))

    # def test_timeout_exception(self, mock_request):
    #     mock_request.side_effect = Timeout
    #     with self.assertRaises(SystemExit) as sysexit:
    #         with self.assertRaises(Timeout):
    #             request_image_search_url(self.url, self.img)
    #         self.assertTrue(isinstance(sysexit, SystemExit))



@patch('app.image_downloader.bs4.BeautifulSoup')
@patch('app.image_downloader.requests.get')
class BeautifulSoupTest(TestCase):
    """
    Test that a beautiful soup object is created when passed the response from
    request.get() using the create_beautifulsoup_object() func.
    """

    def test_create_beautifulsoup_object(self, mock_request, mock_bs4):
        url = IMAGE_SEARCH_ENGINE_URL
        img = IMAGE_TO_SEARCH

        # First create a valid response object   
        mock_response = Mock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response 
        response = request_image_search_url(url, img)
        print(f'\n\nRESPONSE type: {type(response)}')

        mock_bs4.return_value = response
        # pass object to patched create_beautifulsoup_object
        soup = create_beautifulsoup_object(response)
        print(f'SOUP TYPE: {type(soup)}')
        
        


        # mock_request = pass
        # mock_bs4 = pass





        # response = request_image_search_url(url, img)
        # create_beautifulsoup_object = Mock(spec_set=True)
        # soup = create_beautifulsoup_object(response)
        # # soup = Mock(spec_set=bs4.BeautifulSoup)
        # self.assertTrue(isinstance(soup, bs4.BeautifulSoup))

        # XXX: use return value on a mock to return a mock



        # response = request_image_search_url(url, img)
        # soup = create_beautifulsoup_object(response)
        # # soup = Mock(spec_set=bs4.BeautifulSoup())
        # print(f'\n\nresponse type = {type(response)}')
        # print(f'soup type = {type(soup)}')
        # self.assertTrue(isinstance(soup, bs4.BeautifulSoup))


    # XXX: Works, needs to be mocked out
    # def test_create_beautifulsoup_object(self):
    #     soup = create_beautifulsoup_object(request_image_search_url(
    #         IMAGE_SEARCH_ENGINE_URL, IMAGE_TO_SEARCH))
    #     self.assertTrue(isinstance(soup, bs4.BeautifulSoup))

    # >>> type(soup)
    # <class 'bs4.BeautifulSoup'>



if __name__ == '__main__':
    unittest.main()

