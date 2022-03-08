import tweepy
import config


def getClient():
  client =tweepy.Client(tweepy.Client(bearer_token=config.BEARER_TOKEN)
                                   # consumer_key=config.API_KEY,consumer_secret=config.API_KEY_SECRET,
                                   # access_token=config.ACCES_TOKEN,
                                    #access_token_secret=config.ACCES_TOKEN_SECRET))

  return client



def getUserInfo():
    client = getClient()
    user = client.get_user(username='FabienHoti')

    return user

#user = getUserInfo()

#print(user)
