#!/usr/bin/env python

"""
Prompt user for a type of image to search for, the navigate to search engine
and download first 4 pages of images from search results to dump directory.
Search engine: https://depositphotos.com/
"""

import os
import bs4
import requests
import sys
import time
from requests.exceptions import (
    MissingSchema,
    InvalidURL,
    Timeout,
    #ConnectionError
)

# CONSTANTS
IMAGE_SEARCH_ENGINE_URL = 'https://depositphotos.com/stock-photos/'

def user_prompt():
    """
    Prompt user to search for a set of images, and choose where to store them.
    """

    image_to_search = input('What do you want to search for?\nImage search: ')
    filepath = input('Where would you like to store the files? \n'
    'Example: /home/bill/imageFiles/\nPath: ')

    return image_to_search, filepath

def create_repository(filepath):
    """
    Create image file repository based off of answers from user_prompt().
    Change working directory to image file repository.
    """

    os.makedirs(filepath, exist_ok=True)
    os.chdir(filepath)

class InvalidURL(Exception):
    pass

class ServerError(Exception):
    pass

def request_image_search_url(
        image_search_engine_url,
        image_to_search,
        page_index=0,
        attempts=1,
    ):
    """
    Accept image search engine URL, image to search and page index as 
    paramaters. Format URL based off of parameters. Return response from
    requests.get() on URL.
    """

    full_url = (
        f'{image_search_engine_url}{image_to_search}.html?offset={page_index}'
    )
    response_from_request = None
    attempts_left = attempts

    while attempts_left >= attempts:
        attempts_left -= 1
        try:
            response_from_request = requests.get(full_url)
        except InvalidURL:
            print(
                f'Invalid URL: "{full_url}"\nExiting program. Please try again.'
            )
            break
        except Timeout:
            print(
                f'Timeout encountered, retrying. Attempts left: {attempts_left}'
            )
            time.sleep(10)
            continue
        except Exception as e:
            print(f'Something went wrong. Error message: "{e}"')
            break
        
    if not response_from_request:
        print('Did not receive a response from request. Exiting program.')
        sys.exit()

    retval = response_from_request.status_code
    if retval == 200:
        return response_from_request
    elif retval >= 400 and retval < 500:
        print(
            f'There was an error with your request. Status code: {retval}'
        )
        sys.exit()
    elif retval >= 500:
        print(f'Server encountered an error. Status code: {retval}')
        sys.exit()

def create_beautifulsoup_object(response_from_request):
    """
    Return html-parsed BeautifulSoup object
    for image search. Soup object will contain references to ~100 images.    """

    return bs4.BeautifulSoup(response_from_request.text, 'html.parser')

def scrape_image_urls_and_append_to_list(soup):
    """
    Accept beautifulsoup object as paramater. Scrape object for image urls and
    append to a list. Return list.
    """

    images_regular = soup.find_all('img', attrs={
        'class':'file-container__image _file-image'})
    images_lazy_load = soup.find_all('img', attrs={
        'class':'file-container__image _file-image lazyload'})
    image_list = []
    for image in images_regular:
        image_list.append(image.get('src'))
    for image in images_lazy_load:
        image_list.append(image.get('data-src'))

    return image_list

def download_images(image_list):
    """
    Accept image list and filepath as parameters. Iterate through list and
    download each item to working dir, which will be image_dump repository.
    """

    for image in image_list:
        if "http" in image:
            with open(os.path.basename(image), "wb") as file:
                file.write(requests.get(image).content)

def delete_zero_byte_images():
    """
    Delete images that are zero bytes in size in the event they were
    downloaded by mistake.
    """

    for file in os.listdir():
        if os.path.getsize(file) == 0:
            os.remove(file)

def 

if __name__ == "__main__":
    print('Welcome to Image Downloader!')
    print('Image search engine: depositphotos.com')
    print('Image Downloader will download 4 pages of images from the search'
            ' of your choice.')
    image_to_search, filepath = user_prompt()
    create_repository(filepath)

    # run loop 4 times; offset needs to increase in increments of 100
    print('Downloading images. This may take a few minutes...')
    for iter in range(0, 400, 100):
        response_from_request = request_image_search_url(
            IMAGE_SEARCH_ENGINE_URL, image_to_search, iter
        )
        soup = create_beautifulsoup_object(response_from_request)
        image_list = scrape_image_urls_and_append_to_list(soup)
        download_images(image_list)
    delete_zero_byte_images()
    print('-' * 50,'\nDownload finished! Exiting program.')

# Easy copy and paste for image repo:
# /home/ross/AllThingsPython/MyDev/scrape_and_tweet/image_dump/
