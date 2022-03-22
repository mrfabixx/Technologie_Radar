from textblob import TextBlob
import config
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

def getClient():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)#consumer_key=config.API_KEY,consumer_secret=config.API_KEY_SECRET,acces_token=config.ACCESS_TOKEN,acces_token_secret=config.ACCESS_TOKEN_SECRET)

    return client

def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+','',text)  #remove.substring mentions
    text = re.sub(r'#','',text) #removing the # symbol
    text = re.sub(r'RT[\s]+','',text) #remove RT
    text= re.sub(r'https?:\/\/S+','',text)  #remove hyper link'
    return text


def searchTweets(query):  # soll eine funktion werden die die keywörter filtert seu es in der haeadline oder im text oder hashtags
    client = getClient()
    #tweets = client.seach_recent_tweets(query=query,max_reuslts=10)

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                        media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                        max_results=10)
    tweet_data = tweets.data
    results=[]

    for tweet in tweet_data:
        if not tweet_data is None and len(tweet_data) > 0:
            obj={}
            obj['id'] = tweet.id
            #obj['username']=tweet.usernames
            obj['text'] = tweet.text
            results.append(obj)

        else:
            return []

    return results


def filter_tweets(query):
    client =getClient()
    tweet = client.search_recent_tweets(query=query, max_results=10)
    result = []
    tweet_text = tweet.data
    for x in tweet_text:
        dic = {}
        dic['text_from_tweet']=x.text
        result.append(dic)
    return result

#----- text ausgeben lassen

ausgabe = filter_tweets("software")
print(ausgabe)


# aufrufen der funktion die ein keyword dursucht

tweets = searchTweets("Bitcoin")
for x in tweets:
    if len(x) > 0:
        print(x)
    else:
        print("No matching tweets")



