import google_file
import reddit_file
import twitter_file
import sideworks_file
import os
import random
import time
from datetime import datetime

def text():
    try:
        random_subreddit_number = random.randint(6 , 7)
        sub = subredditlist[random_subreddit_number]
        subreddit = reddit_file.obtainaing_sub(reddit,sub)
        submission = reddit_file.bestpost(subreddit,postidlist)
        tweet = submission.title + hashtag
        twitter_file.update_status(twitter , tweet)
        postidlist.append(submission.id)
        google_file.update_info(postidlist  , worksheet)
    except Exception as e:
        print("-->Error in post time method of main")
        print(e)

def image():
    try:

        random_subreddit_number = random.randint(0 , 5)
        sub = subredditlist[random_subreddit_number]
        subreddit = reddit_file.obtainaing_sub(reddit,sub)
        submission = reddit_file.bestpost(subreddit,postidlist)
        filename = sideworks_file.download_image(submission.url)
        while (os.stat(filename).st_size > 3000000):
            submission = reddit_file.bestpost(subreddit,postidlist)
            filename = sideworks_file.download_image(submission.url)
        tweet = submission.title + hashtag
        twitter_file.update_status_with_media(twitter , filename , tweet)
        sideworks_file.remove_image(filename)
        postidlist.append(submission.id)
        google_file.update_info(postidlist , worksheet)
    except Exception as e:
        print("-->Error in post time method of main")
        print(e)

def main():
    try:
        while True:
            for i in range(4):
                image()
                time.sleep(10800)
            time.sleep(3600)
            text()
            time.sleep(39600)
    except Exception as e:
        print("-->Error in the driver function")
        print(e)

worksheet = google_file.login_gsheet()
reddit = reddit_file.login_reddit()
twitter = twitter_file.login_twitter()
subredditlist , hastaglist , postidlist = google_file.get_info(worksheet)
day = datetime.today().weekday()
hashtag = hastaglist[day]
print("Let start:")
if __name__ =="__main__":
    main()
