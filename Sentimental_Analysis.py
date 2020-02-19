from tweepy import *
from textblob import TextBlob

consumer_key = 'xxx'            #Enter your username
consumer_secret = 'xxx'         #Enter your password

access_token = 'xxx'            #Obtain it from tweet API
access_token_secret = 'xxx'     #Obtain it from tweet API

try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)      #http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print("Logged In")

except:
    print("Authentication Error")


user_input = input("Enter the subject you want to search about : ")
tweets = api.search(user_input)             #twitter search according the input entered by the user

for tweet in tweets:
    tweet_text = tweet.text                 #https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
    print(tweet_text)

    analysis = TextBlob(tweet_text)

    tweet_polarity = analysis.sentiiment.polarity
    print(tweet_polarity)

    if tweet_polarity > 0.0:
        print("POSITIVE")
    elif tweet_polarity < 0.0:
        print("NEGATIVE")
    else:
        print("NEUTRAL")
