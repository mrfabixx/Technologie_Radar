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




def get_user_information(username):
    client = getClient()
    user = client.get_users(usernames=["FabienHoti"])
    user_info=[]

    for x in user:
        dic = {}
        dic['id']=x.id
        dic['username']=x.usernames
        user_info.append(dic)
    return user_info



#---------------- aufrufen von user info die man eingibt
#user_info = get_user_information("FabienHoti")













#def ():   #soll likes von posts und retweets raussuchen









