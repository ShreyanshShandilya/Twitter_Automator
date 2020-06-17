import tweepy
import os

def login_twitter():
    print("\t\t**Login twitter")
    try:
        auth = tweepy.OAuthHandler(os.environ['consumer_token'],os.environ['consumer_secret'])
        auth.set_access_token(os.environ['twitter_key'],os.environ['twitter_secret'])
        twitter =tweepy.API(auth)
        return twitter
    except Exception as e:
        print(e)
        print("Exception in twitter authentication function")

def update_status(twitter,tweet):
    print("twitter update status")
    try:
        twitter.update_status(tweet[:280])
    except Exception as e:
        print("Exception in updating status on twitter")
        print(e)

def update_status_with_media(twitter,filename,tweet):
    print("twitter update media")
    try:
        twitter.update_with_media(filename,status=tweet[:280])
    except Exception as e:
        print("Exception in posting image on twitter")
        print(e)
