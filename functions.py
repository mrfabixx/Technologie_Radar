import tweepy
import config

client =tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'bitcoin'

#response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], expansions=['author_id'])

#counts = client.get_recent_tweets_count(query=query, granularity='day')
users = client.get_users(usernames=['FabienHoti'])
for x in users:
    print(x)



'''for x in response.includes:
    x.append()
    print(users)

for tweet in response.data:
    if len(tweet) > 0:
        print(tweet.id)
        print(tweet.lang)

'''

