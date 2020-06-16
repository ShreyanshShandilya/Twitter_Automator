import google_file
import reddit_file
import twitter_file
import mail_file
import sideworks_file
import joke_file
import os
import random
import time

def main():
    print("\t\t\t ***MAIN FUNCTION***")
    try:
        while True:
            #Phase1
            #Creating objects of gsheet reddit and twitter
            worksheet = google_file.login_gsheet()
            reddit = reddit_file.login_reddit()
            twitter = twitter_file.login_twitter()
            #Phase2
            #Fetching emailid postid and redditpostid from gsheet
            EMAIL_ID , POST_ID_JOKE , REDDIT_POST_ID =google_file.get_info(worksheet)
            #Removing blank spaces from list
            EMAIL_ID = google_file.list_beautify(EMAIL_ID)
            POST_ID_JOKE = google_file.list_beautify(POST_ID_JOKE)
            REDDIT_POST_ID =  google_file.list_beautify(REDDIT_POST_ID)
            #Obtaining subreddit
            subreddit = reddit_file.obtainaing_sub(reddit,"wallpaper")
            #Obtaining submission from subreddit
            submission = reddit_file.bestpost(subreddit,REDDIT_POST_ID)
            #Downloading image from submission
            filename = sideworks_file.download_image(submission.url)
            #Checking if filesize is > 3 MB as twitter allows only 3MB
            while (os.stat(filename).st_size > 3000000):
                submission = reddit_file.bestpost(subreddit,REDDIT_POST_ID)
                filename = sideworks_file.download_image(submission.url)
            #Uploading the file to twitter
            twitter_file.update_status_with_media(twitter , filename , (submission.title +"u/" +submission.author.name +" #wallpaper"))
            #Adding submission id to postid list
            REDDIT_POST_ID.append(submission.id)
            #Fetching joke from API
            json_joke = joke_file.joke(POST_ID_JOKE)
            #Adding joke id to list
            POST_ID_JOKE.append(json_joke['id'])
            #Sending mail to mail ids from emailidlist
            mail_file.send_mail("Your daily wallpaper and dad joke" , json_joke['joke'] ,filename,EMAIL_ID)
            #Phase3
            #Removing image from computer
            sideworks_file.remove_image(filename)
            #updating sheet in google sheet
            google_file.update_info(POST_ID_JOKE , REDDIT_POST_ID , worksheet)
            #Value in seconds
            #Script so that it runs once a day
            time.sleep(random.randint(43200,86400))
    except Exception as e:
        print("Exception in main Function")
        print(e)

if __name__ =="__main__":
    main()
