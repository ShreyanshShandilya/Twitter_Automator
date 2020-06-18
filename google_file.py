import pygsheets
import os

def login_gsheet():
    print("-->Login spreadsheet")
    try:
        #Google-crredentials.json file is created at runtime using buildpack which uses environment variable
        gs = pygsheets.authorize(service_file = 'google-credentials.json')
        #Open takes name of sheet as input
        sh = gs.open('heroku_twitter_mail_Database')
        #[1] -> The second sheet
        worksheet = sh.worksheets()[1]
        return worksheet
    except Exception as e:
        print("<>Exception in login google sheet function")
        print(e)

#Fetching data from worksheet
def get_info(worksheet):
    print("-->Fetching spreadsheet")
    try:
        subredditlist = worksheet.get_col(1)
        hastaglist = worksheet.get_col(2)
        postidlist = worksheet.get_col(3)
        subredditlist = list_beautify(subredditlist)
        hastaglist = list_beautify(hastaglist)
        postidlist = list_beautify(postidlist)
        return (subredditlist , hastaglist , postidlist)
    except Exception as e:
        print("<>Exception in fetching the worksheet")
        print(e)

#Updating worksheet
def update_info(postidlist , worksheet):
    print("-->Updating spreadsheet")
    try:
        worksheet.update_col(3,postidlist)
    except Exception as e:
        print("<>Exception in updating worksheet")
        print(e)

#Removing blank spaces
def list_beautify(L1):
    print("-->Removing blank spaces")
    try:
        l1 = list()
        for i in L1:
            if i != "":
                l1.append(i)
        return l1
    except Exception as e:
        print("<>Exception in list beautify method")
        print(e)
