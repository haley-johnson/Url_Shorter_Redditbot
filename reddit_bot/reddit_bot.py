import praw
import config
import time
import os
import requests
import re
import json


def bot_login():
    print ("Logging in to Reddit...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "URL shortener")
    print ("Logged in!")

    return r

def run_bot(r, comments_replied_to):
    

    found_url = ""
    print("Grabbing 30 comments!")
    #Subreddit can be changed to any subreddit that is preferred
    for comment in r.subreddit('testingground4bots').comments(limit = 30):
        if "!shortenurl" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("String with \"!shortenurl\" found in comment " + comment.id)
                
            comment_reply = "You requested to shorten your URL! Here is the new URL:\n\n"

            #retrieves the URL stored in the body of the comment
            found_url = (re.search("(?P<url>https?://[^\s]+)", comment.body).group("url"))
            
            #the base URL of the site on which my current API is hosted, can be changed to any API site 
            url2 = "'https://j-pqpz.onrender.com/"
            #the URL for POST request to retrieve shortened URL
            URL = 'https://j-pqpz.onrender.com/shortUrls'
            #fullUrl is the initial url in comment body
            PARAMS = {'fullUrl': found_url}
            #to receive json response and give type of request
            headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'}
        
            #the last dictionary of the json response is where the short URL is stored
            new = requests.post(url = URL, data = PARAMS, headers = headers).json()[-1]['short']

            #comment response
            comment_reply += ">" + (url2 + new) + "\n\n (apologies - this URL might seem a little long due the base URL of the site I am hosting the API on, this bot is currently for my testing purposes! :) )"

            comment.reply(comment_reply)
            print ("Replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print ("Sleeping for 5 seconds")
    time.sleep(5)

#to ensure that comments are only replied to once, the unique comment ID is saved in a file 
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

#to keep continuously running
while True:
    run_bot(r, comments_replied_to)