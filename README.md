# Twitter-Sentimental-Analysis
Using twitter api and python libraries to predict if a tweet is positive, negative or neutral.

Installing twitter API
pip install tweepy

Installing TextBlob python library
pip install textblob

You should be good to go now. 

Eg of how textblob works:
-> sentence = TextBlob("A rational politician is bad for any country")
-> result = sentence.sentiment.polarity
#result will be a number ranging between -1.0 to 1.0.
You can decide the sentiment of a tweet using the polarity or subjective sentiment provided by textblob library.

Refer to the documentation for more clear definition:
https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
