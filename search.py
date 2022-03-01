import tweepy
import config

client = tweepy.Client(bearer_token=config.Bearer_Token)

client.get_liking_users(id=config.tweet_id)
users = client.get_liking_users(id=config.tweet_id)   #wer hat diesen tweet gliked
users_1 = client.get_retweeters(id=config.tweet_id)   #user die retweet haben

response = client.get_tweet(id=config.tweet_id, tweet_fields=["created_at"])
#for user in users_1.data:
 #   print(user.id)
print(response)
"""
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
