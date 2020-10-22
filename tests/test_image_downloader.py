"""
Unittest based test framework for functions in app.image_downloader.py
"""

import os
import bs4
import requests
import pytest
import unittest
from unittest import mock, TestCase
from unittest.mock import patch
from app.image_downloader import (
    user_prompt,
    create_repository,
    navigate_to_image_search_engine_url,
    create_beautifulsoup_object,
    scrape_image_urls_and_append_to_list,
    download_images,
    delete_zero_byte_images,
)

# CONSTANTS
TEMP_FILEPATH = '/home/ross/AllThingsPython/MyDev/scrape_and_tweet/temp_dir'
IMAGE_SEARCH_ENGINE_URL = 'https://depositphotos.com/stock-photos/'

class TestUserPrompt(TestCase):
    """
    Test image_to_search and filepath input functionality for 
    image_downloader.user_prompt()
    """
    pass

class TestImageRepositoryCreation(TestCase):
    """
    Test image_downloader.create_repository() func, which will also chdir to
    directory. Verify directory was created and is then current working dir.
    Delete directory when finished and verify it was deleted.
    """

    def setUp(self):
        pass

    def tearDown(self):
        os.chdir('..')
        os.rmdir(TEMP_FILEPATH)
        self.assertNotIn(TEMP_FILEPATH, os.listdir())

    def test_can_create_image_repository(self):
        create_repository(TEMP_FILEPATH)
        self.assertEqual(os.getcwd(), TEMP_FILEPATH)

class TestNavigateToImageSearchEngineUrl(TestCase):
    """
    Test 
    """
    pass

if __name__ == '__main__':
    unittest.main()

