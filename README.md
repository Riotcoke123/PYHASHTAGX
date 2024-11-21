<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>
    <h1>Python Twitter/X HASHTAG RETWEETS</h1>
    <p>This repository contains a Python script that automates retweeting tweets containing specified hashtags from Twitter (X). The script uses the <strong>Tweepy</strong> library to interact with the Twitter API, search for tweets with specific hashtags, and retweet them. It supports multiple hashtags, such as <code>#Python</code>, <code>#ip2</code>, <code>#NBA</code>, and <code>#MLB</code>, and can be easily configured to retweet tweets based on user-defined hashtags.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Automated Retweets</strong>: Automatically retweets tweets containing any of the specified hashtags.</li>
        <li><strong>Multiple Hashtags</strong>: Supports searching and retweeting tweets with multiple hashtags, such as <code>#Python</code>, <code>#NBA</code>, <code>#MLB</code>, and more.</li>
        <li><strong>Customizable</strong>: Easily modify the number of tweets to retweet or change the hashtags.</li>
        <li><strong>Error Handling</strong>: Handles errors gracefully (e.g., already retweeted tweets, deleted tweets).</li>
    </ul>
    <h2>Requirements</h2>
    <p>Before using the script, ensure that you have the following:</p>
    <ul>
        <li><strong>Python 3.x</strong> installed.</li>
        <li><strong>Tweepy</strong> library installed. If you haven't installed it yet, you can install it via pip:</li>
    </ul>
    <pre><code>pip install tweepy</code></pre>
    <h2>Setup</h2>
    <ol>
        <li><strong>Install the necessary libraries</strong> by running the command:</li>
        <pre><code>pip install tweepy</code></pre>
        <li><strong>Set up your Twitter Developer Account</strong>:
            <ul>
                <li>Create a Twitter Developer account and create an app at <a href="https://developer.twitter.com/en/apps" target="_blank">Twitter Developer Dashboard</a>.</li>
                <li>Obtain your <strong>API Key</strong>, <strong>API Secret Key</strong>, <strong>Access Token</strong>, and <strong>Access Token Secret</strong> from the Developer Dashboard.</li>
            </ul>
        </li>
        <li><strong>Replace the placeholder credentials</strong> in the Python script with your API keys and tokens.</li>
        <li><strong>Run the script</strong> to start retweeting tweets with the specified hashtags.</li>
    </ol>
    <h2>Usage</h2>
    <p>The script allows you to define the hashtags you want to track and retweet. The following sample code searches for tweets with the hashtags <code>#Python</code>, <code>#ip2</code>, <code>#NBA</code>, and <code>#MLB</code> and retweets the first 10 tweets:</p>
    <pre><code>
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
    </code></pre>
    <h2>Important Notes</h2>
    <ul>
        <li><strong>Rate Limits:</strong> Be aware of Twitter's rate limits and quota system. Exceeding the rate limits may result in temporary suspension of API access. You can read more about Twitter's rate limits in their <a href="https://developer.twitter.com/en/docs/rate-limits" target="_blank">Rate Limit Documentation</a>.</li>
        <li><strong>Twitter Developer Account:</strong> Make sure you follow Twitter's guidelines and rules to avoid violating the platform's terms of service.</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>
    <h2>Credits</h2>
    <p>This script was created by <strong>Riotcoke123</strong>. Special thanks to the <a href="https://www.tweepy.org/" target="_blank">Tweepy</a> library for making Twitter API interaction easier.</p>
</body>
</html>
