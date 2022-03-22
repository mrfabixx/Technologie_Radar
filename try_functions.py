import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)



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

    return positive_list, negative_list, neutral_lis