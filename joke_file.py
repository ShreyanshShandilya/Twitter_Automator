import requests
import os

def joke(POST_ID_JOKE):
    while True:
        URL = "https://icanhazdadjoke.com/"
        headers = {'Accept':'application/json'}
        r = requests.get(URL , headers = headers)
        json_joke = r.json()
        if json_joke['id'] not in POST_ID_JOKE:
            return json_joke
