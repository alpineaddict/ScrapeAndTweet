#!/usr/bin/env python

'''
Prompt user for a type of image to search for, the navigate to search engine
and download first 4 pages of images from search results to dump directory.
Search engine: https://depositphotos.com/
'''

import os
import bs4
import requests

def user_prompt():
    '''
    Prompt user to search for a set of images, and choose where to store them.
    '''

    image_search = input('\nWhat do you want to search for?\nImage search: ')
    filepath = input('Where would you like to store the files? \n'
    'Example: /home/bill/imageFiles/\nPath: ')

    return image_search, filepath

def create_repository(filepath):
    '''
    Create image file repository based off of answers from user_prompt().
    '''

    os.makedirs(filepath, exist_ok=True)
    os.chdir(filepath)

def image_scrape(image_search):
    '''
    Accept URL as parameter and download roughly 300-400 images (4 pages)
    from search results.
    '''

    counter = 0
    image_list = []
    for iter in range(4):
        website_url =(f'https://depositphotos.com/stock-photos/{image_search}'
        f'.html?offset={counter}')
        res = requests.get(website_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Scrapes 100 images (different source tags). Add objects to list
        images_regular  = soup.find_all('img', attrs={'class':
                                'file-container__image _file-image'})
        images_lazy_load = soup.find_all('img', attrs={'class':
                                'file-container__image _file-image lazyload'})
        for image in images_regular:
            image_list.append(image.get('src'))
        for image in images_lazy_load:
            image_list.append(image.get('data-src'))
        counter += 100
    return image_list

def delete_zero_byte_images(filepath):
    '''
    Delete images that are zero bytes in size in the event they were
    downloaded by mistake.
    '''

    for file in os.listdir(filepath):
        if os.path.getsize(file) == 0:
            os.remove(file)

def image_download(image_list, filepath):
    '''
    Scrape images and download to specified file path.
    Delete any zero byte files.
    '''

    print('Downloading images. This may take a few minutes...')
    for image in image_list:
        if "http" in image:
            with open(os.path.basename(image), "wb") as f:
                f.write(requests.get(image).content)
    print('-' * 50)
    delete_zero_byte_images(filepath)
    print('\nDownload finished! Exiting program.')


if __name__ == "__main__":
    print('Welcome to Image Downloader!')
    print('Image search engine: depositphotos.com')
    print('Image Downloader will download 4 pages of images from the search'
            'of your choice.')
    image_search, filepath = user_prompt()
    create_repository(filepath)
    image_list = image_scrape(image_search)
    image_download(image_list, filepath)

# Easy copy and paste for image repo:
# /home/ross/AllThingsPython/MyDev/ScrapeAndTweet/ImageDump/
