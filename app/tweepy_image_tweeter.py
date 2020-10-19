#!/usr/bin/env python3

"""
Specifically designed to interact with @soomanypugs twitter account.
Built on contingency of run-thru of sister ImageDownloader.py script.
When executed, log into twitter via API and tweet a random picture of a pug
from image repository. Image is then deleted (sent to trash/recycle).
"""

import os
import random
import sys
import time
import send2trash
import tweepy
import config

class TweepyAPI():
    """
    Build out API object to interact with Tweepy API & @soomanypugs acccount.
    Authenticate to Twitter Tweepy API.
    """
    def __init__(
            self, api_key, api_secret_key, access_token, access_token_secret
        ):
        self.api_key             = api_key
        self.api_secret_key      = api_secret_key
        self.access_token        = access_token
        self.access_token_secret = access_token_secret

        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

        try:
            print("Attempting authentication...")
            self.api.verify_credentials()
            print("Authentication: OK")
        except tweepy.TweepError:
            print('ERROR! Authentication failure! Shutting down script.')
            sys.exit()

    def tweet_image(self):
        """
        Choose image at random from image repository and tweet it.
        Print image name.
        """
        self.image_list = []
        for image in os.listdir():
            self.image_list.append(image)

        self.image_num = random.randrange(len(self.image_list))
        self.filename = self.image_list[self.image_num]

        try:
            print("Attempting image tweet...")
            self.api.update_with_media(self.filename,status=
            "Via Tweepy API for Python.")
            time.sleep(5)
            print(f"Image '{self.filename}' tweeted successfully.")
        except tweepy.TweepError as e:
            print(f"ERROR! Image file was not uploaded. Error message:\n{e}")
            sys.exit()

    def delete_image(self):
        """
        Delete image and send to trash.
        """
        print("Deleting image file...")
        try:
            send2trash.send2trash(self.filename)
        except OSError as e:
            print(f"Error! File not deleted.\nError Message: {e}")

def navigate_to_image_repository(filepath):
    """
    This is contingent on existing structure and image repository
    with image files!
    """
    try:
        os.chdir(filepath)
    except FileNotFoundError:
        print('Path is invalid. Closing application')
        sys.exit()


if __name__ == '__main__':
    tweepy_tweet = TweepyAPI(
                            config.api_key,
                            config.api_secret_key,
                            config.access_token,
                            config.access_token_secret
    )
    FILEPATH = "/home/ross/AllThingsPython/MyDev/scrape-and-tweet/ImageDump/"

    navigate_to_image_repository(FILEPATH)
    tweepy_tweet.tweet_image()
    tweepy_tweet.delete_image()
    print('Exiting application.')
