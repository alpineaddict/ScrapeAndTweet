"""
Unittest based test framework for functions in app.tweepy_image_tweeter.py
"""

import os
import random
import sys
import time
import send2trash
import tweepy
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from requests.exceptions import InvalidURL, Timeout
from app.tweepy_image_tweeter import TweepyAPI, navigate_to_image_repository
import test_config

# CONSTANTS
TEMP_FILEPATH = '/home/ross/AllThingsPython/MyDev/scrape_and_tweet/temp_dir'

# Create simulation tweepy object
tweepy_test_obj = TweepyAPI(
                        test_config.api_key,
                        test_config.api_secret_key,
                        test_config.access_token,
                        test_config.access_token_secret
)

tweepy_test_obj.user_login()

# XXX: This test is successful; uncomment when finished
# class TestChdir(TestCase):
#     """Test image repository functions."""
#     @patch('app.tweepy_image_tweeter.os.chdir', side_effect=TEMP_FILEPATH)
#     def test_can_chdir_to_image_repository(self, mock_chdir):
#         navigate_to_image_repository(TEMP_FILEPATH)
#         mock_chdir.assert_called_with(TEMP_FILEPATH)

#     def test_file_not_found_exception(self):
#         with self.assertRaises(SystemExit) as sysexit:
#             with self.assertRaises(FileNotFoundError):
#                  navigate_to_image_repository('/invalidpath')
#             self.assertTrue(isinstance(sysexit, SystemExit))


class TestTweepyObjectMethods(TestCase):
    """Test methods on tweepy class object."""
    def test_user_login(self):
        tweepy_test_obj.user_login()

#     def login_failure(self):
#         pass

#     def test_tweet_image(self):
#         pass

#     def test_delete_image(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()