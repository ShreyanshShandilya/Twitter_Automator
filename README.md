With about 15% of Twitter being composed of bots, I wanted to try my hand at it.

# Twiiter Profile: [NineBit](https://twitter.com/__NineBit)

## Disclaimer

I hold no liability for what you do with this script or what happens to you by using this script. Abusing this script can get you banned from Twitter, so make sure to read up on proper usage of the Twitter API.

# Setup
Download all the required packages
* `pip install tweepy`
* `pip install pygsheets`
* `pip install praw`
* `pip install wget`
***
# Credentials

### Next, we need to link our Twitter account to our Python script. Go to [Twitter Developers](apps.twitter.com) and sign in with your account. Create a Twitter application and generate a Consumer Key, Consumer Secret, Access Token, and Access Token Secret. 

### Obtain OAuth2 credentials from [Google Developers Console](https://console.developers.google.com/) for google spreadsheet api and drive api and save the file as `google-credentials.json`

### Obtain credentials from [Reddit preferences](https://www.reddit.com/prefs/apps/) for reddit api.
***
# Libraries 

### Tweepy:An easy-to-use Python library for accessing the Twitter API.
* To post tweets.
* To like all tweets posted.

### Pygsheets:A simple, intuitive python library to access google spreadsheets through the Google Sheets API v4.
* To maintain records of all tweets posted.
* To avoid  duplicate tweets

### Praw:The Python Reddit API Wrapper
* To search for submission within subreddits.

### Wget:GNU Wget is a computer program that retrieves content from web servers.
* To download image from reddit.
***
# Heroku

To host python script on Heroku[Heroku](https://dashboard.heroku.com/) you need to do a few things.
* Define a `requirements.txt` file in the root of your project that lists your dependencies. This is what Heroku will use to 'detect' you're using a Python app.
* Add to Procfile: `worker: python main.py`
* Save all your credentials in *Config Vars* (environment variables).
* To run the app correctly you need to save the content of your google credentials file in a variable named `GOOGLE_CREDENTIALS` and then create another environment variable with key=`GOOGLE_APPLICATION_CREDENTIALS` and value = `google-credentials.json`.
* Then create a buildpack. Instructions [Here](https://github.com/ShreyanshShandilya/heroku-google-application-credentials-buildpack)
***
## Format Google sheet

* Column A contains list of subreddits.
* Column B contains list of hashtag that goes with the tweet.
* Column C contains list of ids of post posted.
***
# Future Work

* To implement ML so that bot posts original content.
* To get meaningful insights on how people post throughout year.


# Wrapping up
This bot will continue to post until Heroku remove its free tier or I run out of Dyno hours.
