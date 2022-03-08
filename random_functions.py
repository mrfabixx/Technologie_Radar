"""
import tweepy
import configparser
import pandas as pd

#------ read configs
config = configparser.ConfigParser()
config.read('config.ini')


api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# -------authentication
authentication = tweepy.OAuthHandler(api_key, api_key_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication)

public_tweets = api.home_timeline()
print(public_tweets[0].text)

# create dataframe

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')
"""
#'----------------------------------------------------------------------- code für verschiedene andwendungen
"""
client = tweepy.Client(bearer_token=config.Bearer_Token)

client.get_liking_users(id=config.tweet_id)
users = client.get_liking_users(id=config.tweet_id)   #wer hat diesen tweet gliked
users_1 = client.get_retweeters(id=config.tweet_id)   #user die retweet haben

response = client.get_tweet(id=config.tweet_id, tweet_fields=["created_at"])
#for user in users_1.data:
 #   print(user.id)
print(response)

query = "covid -is:retweet"

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "lang"], user_fields=["profile_image_url"], expansions=["geo.place_id"])
print(response)

users={u["id"]: u for  u in response.includes["users"]}

for tweet in response.data:
   if users [tweet.author_id]:
        user= users[tweet.author_id]
    print(tweet.id)
    print(user.username)
    print(user.profile_image_url)
file_name="Tweet.txt"
with open(file_name,"a+") as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    #print(tweet.id)
     filehandler.write("Xs\n" % tweet.id)


#list of users that liked a tweet
"""