import tweepy
from textblob import TextBlob
import config_token
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import psycopg2


Client = tweepy.Client(bearer_token=config_token.BEARER_TOKEN)

def searchTweets(query):

    tweets = Client.search_recent_tweets(query=query, max_results=10)
    tweet_data = tweets.data
    results = []

    for tweet in tweet_data:
        if not tweet_data is None and len(tweet_data) > 0:
            results.append(tweet.text)
        else:
            return []



    return results


emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
def cleanText (text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  #remove.substring mentions
    text = re.sub(r'#', '', text) #removing the # symbol
    text = re.sub(r'RT[\s]+', '', text) #remove RT
    text = re.sub(r'http\S+', '', text)  #remove hyper link'
    text = emoji_pattern.sub(r'', text)
    return text



def get_subjectivity(text):
    subjectivity = TextBlob(text).sentiment.subjectivity
    return subjectivity

def get_polarity(text):
    polarity = TextBlob(text).sentiment.polarity

    return polarity



tweets = searchTweets("bitcoin")

String_text = '##ll=='.join(tweets)
String_text_1 = String_text.split('##ll==')
print(String_text_1)
i = 1


for element in String_text_1:
    cleaning_tweet = cleanText(element)
    score_polarity = get_polarity(cleaning_tweet)
    score_subjectivity = get_subjectivity(cleaning_tweet)
    print(str(i) + ') ' + cleaning_tweet )
    print("score_polarity: " + str(score_polarity) + "   -----   " + "score_subjectivity: " + str(score_subjectivity))
    if score_polarity < 0:
        print("Der Tweet ist negativ")
    elif score_polarity > 0:
        print("Der Tweet ist positiv")
    elif score_polarity == 0:
        print("Der Tweet ist neutral")
    print("\n")
    i += 1










