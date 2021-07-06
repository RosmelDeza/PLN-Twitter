# import tweepy
# from tweepy import api
# from tweepy import streaming
# from tweepy import auth
# from tweepy.streaming import Stream
# from autenticate import get_auth

# class TweetsListener(tweepy.StreamListener):
#     def on_connect(self):
#         print("Estoy conectado")

#     def on_status(self, status):
#         print(status.text)

#     def on_error(self, status_code):
#         print("Error", status_code)

# auth = get_auth()
# api = tweepy.API(auth, wait_on_rate_limit_notify=True , wait_on_rate_limit=True)

# stream = TweetsListener()
# streamingApi = tweepy.Stream(auth=api.auth, listener=stream)

# streamingApi.filter(
#     track=["pedro castillo", "keiko"]
# )
# import nltk
# nltk.download('stopwords')

print("frecuente\xa0hsy")