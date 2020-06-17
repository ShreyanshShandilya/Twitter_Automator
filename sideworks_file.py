import os
import wget
import praw
import datetime import date
def download_image(url):
    print("Attempting to download image")
    try:
        if (url.startswith("https://i")):
            filename = wget.download(url)
        else:
            filename = None
        return filename
    except Exception as e:
        print("Error in downloading image")
        print(e)

def remove_image(filename):
    print("Attempting to remove image")
    try:
        if (filename is not None):
            os.remove(filename)
    except Exception as e:
        print("Error in deleting file")
        print(e)

def hashtagteller(hastaglist):
    try:
        today = date.today().weekday()
        return hashtag[today]
    except Exception as e:
        print("Error in hashtagteller function")
        print (e)
