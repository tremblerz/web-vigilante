
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from application.creds import twitter_api
import json
import psycopg2
from textblob import TextBlob

try:
    connection = psycopg2.connect("dbname='webvigilante' user='postgres' host='localhost' password='postgre$'")
except Exception as e:
    print("Error: " + e.message)

access_token = twitter_api['access_token']
access_token_secret = twitter_api['access_token_secret']
consumer_key = twitter_api['consumer_key']
consumer_secret = twitter_api['consumer_secret']

def analyze(text):
    sentiment = TextBlob(text)
    polarity = sentiment.polarity
    subjectivity = sentiment.polarity

def store(text):
    sentiment = TextBlob(text)
    polarity = sentiment.polarity
    subjectivity = sentiment.polarity
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tweets (tweet, subjectivity, polarity) VALUES (%s, %s, %s)",
                    (text, polarity, subjectivity))
    connection.commit()
    cursor.close()
    connection.close()

def analyze_and_store_data(tweet_data):
    print(tweet_data['text'] + '\n')
    store(tweet_data['text'])

class StdOutListener(StreamListener):

    def on_data(self, data):
        dict_data = json.loads(data)
        analyze_and_store_data(dict_data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['india'])