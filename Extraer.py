import tweepy
import json
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
# poner todos los nombres juntos con una "" separándolos
#trendsName = " ".join(names)

#evitar el sueño de la api
sleep_on_rate_limit=False

for key in names:
    for tweet in tweepy.Cursor(api.search, q = key, tweet_mode = "extended").items(100):
        print(tweet._json)
        name_file = "tweets/" + tweet._json["id_str"] + ".json"
        print("============================================================================")
        with open(name_file, 'a') as file:
            json.dump(tweet._json, file, indent=4)








