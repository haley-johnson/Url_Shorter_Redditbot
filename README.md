# URL Shortener API + Reddit Bot

## Project Description
> API to create short URLs using NodeJS, Express and MongoDB. Reddit bot created with Python that responds to comments that contain '!shortenurl' in a desired subreddit. It will then reply to the comment with a shortened version of the URL that was included in the body of the user's comment. The reddit bot sends a POST request to the API with the user's long URL and receives the short URL as a response, which it then replies to the user requesting a shortened URL.


## My Deployed API and Reddit Bot
I deployed my API on render -> https://j-pqpz.onrender.com/

Below I have included a screenshot of my reddit bot responding to a users comment. 

[![2023-01-01-22-06-22-3-Test-testingground4bots.png](https://i.postimg.cc/Kz2TJbMy/2023-01-01-22-06-22-3-Test-testingground4bots.png)](https://postimg.cc/CZcdxW7v)

## Quick Start

```bash
# Install dependencies for the API
npm install

# Edit the server.js file in the url-shortener folder with your mongoURI 
# Edit the config.py file in the reddit_bot folder with your reddit account username, password, client_id, client_secret 
# Edit the reddit_bot.py file in the reddit_bot folder with the baseURL of the API 

# Run API
npm run devStart 

# Run Reddit bot
python -u "reddit_bot.py"


