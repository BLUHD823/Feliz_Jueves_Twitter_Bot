import tweepy
from time_stamp import *
from image_paths import *
import schedule
import time

api_key = "API_KEY"
api_secret = "API_SECRET"
bearer_token = r"BEARER_TOKEN"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"
client_id = "CLIENT_ID"
client_id_secret = "CLIENT_ID_SECRET"


client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def image_upload(path:str):
    print(f"Image path: {path}")
    media_idss = []
    media_upload = api.media_upload(path)
    media_idss.append(media_upload.media_id)
    return media_idss

def bot_tweet():
    fecha_hora_argentina = set_time()
    Feliz_Jueves = horario(fecha_hora_argentina)
    datos = open_json(json_path)
    if Feliz_Jueves in [1,2,3,4,9]:
        image_path = get_path(datos,Feliz_Jueves)
        media_ids = image_upload(image_path)
        #Crear tweet
        #client.create_tweet(text="",media_ids=media_ids)
        print("tweet enviado")
    elif Feliz_Jueves in [5,6,7,8]:
        image_path = get_path(datos,Feliz_Jueves)
        media_ids = image_upload(image_path)
        #client.create_tweet(text="",media_ids=media_ids)
        print("tweet enviado")


schedule.every(1).seconds.do(bot_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

