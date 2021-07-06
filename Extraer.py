import tweepy
import json
import os
from autenticate import get_auth

#Validacion de los Keys
auth = get_auth()
api = tweepy.API(auth, wait_on_rate_limit_notify=True , wait_on_rate_limit=True)

#Encontrar tweets que son tendencia en el momento actual
trends1 = api.trends_place(23424919)
data = trends1[0]
# tomar los trends
trends = data["trends"]
# Poner los trends en una lista
names = [trend["name"] for trend in trends]

# top 5
names = names[:6]
#os.mkdir('tweets')

for key in names:
    # separamos temas por carpetas
    carpeta = 'tweets/' + str(key)
    os.mkdir(carpeta)

    for tweet in tweepy.Cursor(api.search, q = key, tweet_mode = "extended", lang = 'es' ).items(5):
        print(tweet._json)
        name_file = carpeta + '/' + tweet._json["id_str"] + ".json"
        print("============================================================================")
        with open(name_file, 'a') as file:
            json.dump(tweet._json, file, indent=4)








