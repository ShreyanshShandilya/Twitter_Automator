import requests
import os

def joke(dadjokelist):
    try:
        while True:
            URL = "https://icanhazdadjoke.com/"
            headers = {'Accept':'application/json'}
            r = requests.get(URL , headers = headers)
            json_joke = r.json()
            if json_joke['id'] not in dadjokelist:
                return json_joke
    except Exception as e:
        print("<>Exception in joke function")
        print(e)
