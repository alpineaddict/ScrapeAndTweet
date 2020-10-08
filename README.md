# scrape-and-tweet
> Application designed to work with Tweepy Twitter API and a web scraper that downloads images. 

This is a two part application intended to be used together, but tweepy_image_tweeter will work with any image repository.  
This is linked to the [@soomanypugs twitter account][soomanypugs].

_How it works?_  
Image downloader will run through a user prompt to inquire of what types of images the user would like to download. Once the input is submitted, the app will download roughly 400 images to an image repository.  

scrape_and_tweet will authenticate to the soomanypugs account, navigate to the image repository and then tweet a random pug image. Once successfully tweeted, the file will be deleted.

### image_downloader.py:  
![](/markdown-screenshots/screenshot1.png)  

### tweepy_image_tweeter.py:
![](/markdown-screenshots/screenshot2.png)

### [@soomanypugs][soomanypugs]:  
![](/markdown-screenshots/screenshot3.png)

## Environment Setup
1. Install Python (Linux-oriented)  
```$ sudo apt-get update```  
```$ sudo apt-get install python3.8```  

2. Set up virtual enivironment (recommended, not required)  
*Version/path dependent on your Python installation*  
```sudo apt-get install python3-pip```  
```pip install virtualenv```  
```python3 -m venv env```  

3. Activate virtual environment from working directory in repository  
```source env/bin/activate```  

4. Install required packages via pip  
```pip install -r requirements.txt```  

## Running the application  
```python image_downloader.py```  
```python tweepy_image_tweeter.py```  

<!-- Markdown link & img dfn's -->
[soomanypugs]:https://twitter.com/soomanypugs
