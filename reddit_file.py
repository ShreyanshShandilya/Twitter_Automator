import praw
import random
import os

def login_reddit():
    print("\t\t***Login reddit")
    try:
        reddit = praw.Reddit(username = os.environ['username'] , password = os.environ['password'] , client_id = os.environ['client_id'] , client_secret = os.environ['client_secret'] , user_agent = "Ninebit")
        return reddit
    except Exception as e:
        print("Exception in reddit authentication function")
        print(e)

def obtainaing_sub(reddit,sub):
    print("reddit subreddit")
    try:
        subreddit = reddit.subreddit(sub)
        return subreddit
    except Exception as e:
        print("Exception in obtainaing subreddit")
        print(e)

def bestpost(subreddit,postidlist):
    print("reddit post")
    try:
        while True:
            posts = [post for post in subreddit.hot(limit=10)]
            random_post_number = random.randint(0, 10)
            submission = posts[random_post_number]
            if submission.id not in REDDIT_POST_ID:
                return submission
    except Exception as e:
        print(e)
        print("Exception in finding best post")
