import pygsheets
import os

def login_gsheet():
    print("\t\t***Login spreadsheet")
    try:
        #Google-crredentials.json file is created at runtime using buildpack which uses environment variable
        gs = pygsheets.authorize(service_file = 'google-credentials.json')
        #Open takes name of sheet as input
        sh = gs.open('heroku_twitter_mail_Database')
        #[0] -> The first sheet
        worksheet = sh.worksheets()[0]
        return worksheet
    except Exception as e:
        print(e)

def get_info(worksheet):
    print("spreadsheet fetch")
    try:
        EMAIL_ID = worksheet.get_col(1)
        POST_ID_JOKE = worksheet.get_col(2)
        REDDIT_POST_ID = worksheet.get_col(3)
        return (EMAIL_ID , POST_ID_JOKE , REDDIT_POST_ID)
    except Exception as e:
        print(e)

def update_info(POST_ID_JOKE , REDDIT_POST_ID , worksheet):
    print("spreadsheet update")
    try:
        worksheet.update_col(2,POST_ID_JOKE)
        worksheet.update_col(3,REDDIT_POST_ID)
    except Exception as e:
        print(e)
#Removing blank spaces
def list_beautify(L1):
    print("removing empty spaces")
    try:
        l1 = list()
        for i in L1:
            if i != "":
                l1.append(i)
        return l1
    except Exception as e:
        print(e)
