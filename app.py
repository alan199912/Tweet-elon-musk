from flask import Flask, jsonify
import tweepy
import configparser
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def get_tweet_elon_musk():

  config = configparser.ConfigParser()
  config.read('config.ini')

  api_key = config['twitter']['api_key']
  api_key_secret = config['twitter']['api_key_secret']

  access_token = config['twitter']['access_token']
  access_token_secret = config['twitter']['access_token_secret']

  auth = tweepy.OAuthHandler(api_key, api_key_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)
  tweet_elon = api.get_user(screen_name='elonmusk')

  tweet = api.search_tweets(q=tweet_elon.status.id, count=1)
  
  return jsonify({
    "id": tweet[0].entities['urls'][0]['expanded_url'].split('status/')[1],
    "tweet": tweet_elon.status.text, 
    "created_at": tweet_elon.status.created_at,
    "score": random.randrange(1, 100),
    "url": tweet[0].entities['urls'][0]['url'],
    "url_embed": f'https://twitter.com/{tweet_elon.screen_name}/status/{tweet_elon.status.id}'
  })

def __main__():
  app.run(debug=True, port=5000)



if __name__ == '__main__':
  __main__()









