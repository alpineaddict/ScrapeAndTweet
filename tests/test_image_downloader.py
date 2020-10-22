"""
Unittest based test framework for functions in app.image_downloader.py
"""

# CONSTANTS
TEMP_FILEPATH = '/home/ross/AllThingsPython/MyDev/scrape_and_tweet/temp_dir'

import os
import bs4
import requests
import pytest
import unittest
from unittest import mock, TestCase
from unittest.mock import patch
from app.image_downloader import image_scrape, create_repository

# TODO: add user prompt test?

class test_image_repository(TestCase):
    """
    Run image_downloader.create_repository() func, which will also chdir to    
    directory. Test that directory was created and is current working dir.
    Delete directory when finished.
    """

    def setUp(self):
        print('Running setUp.')

    def test_can_create_image_repository(self):
        create_repository(TEMP_FILEPATH)
        self.assertEqual(os.getcwd(), TEMP_FILEPATH)

    def tearDown(self):
        print('Running tearDown.')
        os.chdir('..')
        os.rmdir(TEMP_FILEPATH)
        self.assertNotIn(TEMP_FILEPATH, os.listdir())

class test_image_scrape(TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

