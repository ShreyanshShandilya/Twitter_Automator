import tweepy
import os

def login_twitter():
    print("-->Login twitter")
    try:
        auth = tweepy.OAuthHandler(os.environ['consumer_token'],os.environ['consumer_secret'])
        auth.set_access_token(os.environ['twitter_key'],os.environ['twitter_secret'])
        twitter =tweepy.API(auth)
        return twitter
    except Exception as e:
        print(e)
        print("<>Exception in twitter authentication function")

def update_status(twitter,li):
    print("-->Twitter update status")
    try:
        reply_status_id = None
        for sen in li:
            if (reply_status_id is None):
                    reply_status_id = twitter.update_status(sen).id
                    twitter.create_favorite(reply_status_id)
            else:
                    reply_status_id = twitter.update_status(sen , reply_status_id)
                    twitter.create_favorite(reply_status_id)
    except Exception as e:
        print("<>Exception in updating status on twitter")
        print(e)

def update_status_with_media(twitter,filename,tweet):
    print("-->Twitter update media")
    try:
        if(len(tweet) > 280):
            tweet = tweet[:276]+"..."
        id = twitter.update_with_media(filename,status=tweet).id
        twitter.create_favorite(id)
    except Exception as e:
        print("<>Exception in posting image on twitter")
        print(e)

def status_format(tweet):
        tweets = tweet.split()
        sen = ""
        li = list()
        for word in tweets:
            if(len(sen) < 270):
                sen = sen + word + " "
            else:
                sen = sen + "(Cont'd)"
                li.append(sen)
                sen = ""
        else:
            li.append(sen)
        return li
