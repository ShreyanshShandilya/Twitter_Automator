import pygsheets
import os

def login_gsheet():
    print("\t\t-->Login spreadsheet")
    try:
        #Google-crredentials.json file is created at runtime using buildpack which uses environment variable
        gs = pygsheets.authorize(service_file = 'google-credentials.json')
        #Open takes name of sheet as input
        sh = gs.open('heroku_twitter_mail_Database')
        #[1] -> The second sheet
        worksheet = sh.worksheets()[1]
        return worksheet
    except Exception as e:
        print(e)

def get_info(worksheet):
    print("\t-->Fetching spreadsheet")
    try:
        subredditlist = worksheet.get_col(1)
        hastaglist = worksheet.get_col(2)
        postidlist = worksheet.get_col(3)
        dadjokelist = worksheet.get_col(4)
        subredditlist = list_beautify(subredditlist)
        hastaglist = list_beautify(hastaglist)
        postidlist = list_beautify(postidlist)
        dadjokelist = list_beautify(dadjokelist)
        return (subredditlist , hastaglist , postidlist , dadjokelist)
    except Exception as e:
        print(e)

def update_info(postidlist , dadjokelist ,worksheet):
    print("\t-->Updating spreadsheet")
    try:
        worksheet.update_col(3,postidlist)
        worksheet.update_col(4,dadjokelist)
    except Exception as e:
        print(e)
#Removing blank spaces
def list_beautify(L1):
    print("\t-->Removing blank spaces")
    try:
        l1 = list()
        for i in L1:
            if i != "":
                l1.append(i)
        return l1
    except Exception as e:
        print(e)
