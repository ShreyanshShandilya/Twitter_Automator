import yagmail
import os

def send_mail(sub , body , filename , email_list):
    print("\t\t***Sending mail")
    try:
        yag = yagmail.SMTP(user = os.environ['usermail'] , password = os.environ['mailpassword'])
        for i in email_list:
            yag.send( to=i , subject = sub , contents = body , attachments = filename)
    except Exception as e:
        print(e)
