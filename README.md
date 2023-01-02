# URL Shortener Reddit Bot

## Project Description
> API to create short URLs using Node, Express and MongoDB. Reddit bot created with Python that responds to comments that contain '!shortenurl' in a desired subreddit. It will then reply to the comment with a shortened version of the URL that was included in the body of the user's comment. The reddit bot sends a POST request to the API with the user's long URL and recieves the short URL as a response, which it then gives to the user requesting a shortened URL. 
## Quick Start

```bash
# Install dependencies for the API
npm install

# Edit the server.js file in the url-shortener folder with your mongoURI 
# Edit the config.py file in the reddit_bot folder with your reddit account username, password, client_id, client_secret 

# Run API
npm run devStart 

# Run Reddit bot
python -u "reddit_bot.py"

