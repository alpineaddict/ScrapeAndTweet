# scrape-and-tweet
Application designed to work with Tweepy Twitter API and a web scraper that downloads images. 

This is a two part application intended to be used together, but tweepy_image_tweeter will work with any image repository.
This is linked to the @soomanypugs twitter account. 

How it works? 
Image downloader will run through a user prompt to inquire of what types of images the user would like to download. Once the 
input is submitted, the app will download roughly 400 images to an image repository.

tweepy_image_tweeter will authenticate to the soomanypugs account, navigate to the image repository and then tweet a random
pug image. Once successfully tweeted, the file will be deleted.
