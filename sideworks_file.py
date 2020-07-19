import os
import wget
import praw

def download_image(url):
    print("-->Attempting to download image")
    try:
        filename = wget.download(url)
        return filename
    except Exception as e:
        print("<>Error in downloading image")
        print(e)

def remove_image(filename):
    print("-->Attempting to remove image")
    try:
        if (filename is not None):
            os.remove(filename)
    except Exception as e:
        print("<>Error in deleting file")
        print(e)
