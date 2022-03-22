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

class TwitterClient(Object):

    def __init__(self):
        consumerKey = config.API_KEY
        consumerSecret = config.API_KEY_SECRET
        accessToken = config.ACCESS_TOKEN
        accessTokenSecret = config.ACCESS_TOKEN_SECRET
        try:
            auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            auth.set_access_token(accessToken, accessTokenSecret)
            self.api = tweepy.API(auth)
        except:
            print("authenfication is not provided")


    def get_tweets(self,query,count=0):
        tweets=[]

        fetched_tweets =  self.api.search_tweets(q=query,count =count)
        for tweet in fetched_tweets:
            dic ={}
            dic['text']=tweet.text
            dic['sentiment']=tweet.get_tweet_sentiment
            if tweet.retweet.count > 0




def sentiment_analyser(tweet):

    tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(tweet_count)
    negativ = 0
    positiv = 0
    neutral = 0

    tweet_list = []
    neutral_list = []
    negative_list = []
    positive_list = []

    for tweet in tweets:
        print(tweet)
        tweet_list.append(tweet.text)
        analysis = TextBlob(tweet.text)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)

    if score < 0:
        negative_list.append(tweet.text)
        negativ += 1

    elif score > 0:
        positive_list.append(tweet.text)
        positiv += 1

    elif score == 0:
        neutral_list.append(tweet.text)
        neutral += 1


















