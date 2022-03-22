import tweepy
from textblob import TextBlob
import config
from wordcloud import WordCloud
import pandas as pd # this is used for the dataframe
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


consumerkey = config.API_KEY
consumerkey_secret = config.API_KEY_SECRET
accesToken = config.ACCESS_TOKEN
accesToken_secret = config.ACCESS_TOKEN_SECRET

authenticate = tweepy.OAuthHandler(consumerkey,consumerkey_secret)
authenticate.set_access_token(accesToken,accesToken_secret)

api = tweepy.API(authenticate, wait_on_rate_limit=True)

posts = api.user_timeline(screen_name="BillGates", count=100, tweet_mode="extended") #lang = language
i = 1
print("show the 5 recent tweets: \n ")
for tweet in posts[0:5]:
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i+1

def cleanText (text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  #remove.substring mentions
    text = re.sub(r'#', '', text) #removing the # symbol
    text = re.sub(r'RT[\s]+', '', text) #remove RT
    text = re.sub(r'http\S+', '', text)  #remove hyper link'
   # text = emoji_pattern.sub(r'', text)
    return text
#create Dataframe
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
print(df)

df['Tweets'] = df['Tweets'].apply(cleanText)
print(df)

def get_subjectivity(text):
    subjectivity = TextBlob(text).sentiment.subjectivity
    return subjectivity

def get_polarity(text):
    polarity = TextBlob(text).sentiment.polarity

    return polarity


df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] =df['Tweets'].apply(get_polarity)

print(df)
