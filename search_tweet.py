import tweepy
import config
import json


def getClient():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
                           #consumer_key=config.API_KEY,
                           #consumer_secret=config.API_KEY_SECRET,
                           #acces_token=config.ACCESS_TOKEN,
                           #acces_token_secret=config.ACCESS_TOKEN_SECRET)

    return client

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
            obj['text'] = tweet.text
            results.append(obj)

        else:
            return []
    return results



#---------- aufrufen der funktion die ein keyword dursucht
tweets = searchTweets("Bitcoin")
for x in tweets:
    if len(tweets) > 0:
        print(x)
    else:
        print("No matching tweets")