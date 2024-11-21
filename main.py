import tweepy

# Replace these with your own credentials
API_KEY = 'your-api-key'
API_SECRET_KEY = 'your-api-secret-key'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY, 
    consumer_secret=API_SECRET_KEY, 
    access_token=ACCESS_TOKEN, 
    access_token_secret=ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# Define the hashtags you want to search for
hashtags = "#Python OR #ip2 OR #NBA OR #MLB"

# Search for tweets with the hashtags
tweets = tweepy.Cursor(api.search_tweets, q=hashtags, lang="en").items(10)  # Modify 'items(10)' for the number of tweets

# Retweet each tweet
for tweet in tweets:
    try:
        print(f"Retweeting: {tweet.text}")
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(f"Error while retweeting: {e}")
