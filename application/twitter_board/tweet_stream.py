from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from application.creds import twitter_api, database_details
import json
import psycopg2
from textblob import TextBlob
import re
import string


try:
    connection = psycopg2.connect("dbname='" + database_details['db_name'] + "' user='" +
     database_details['db_user'] + "' host='" + database_details['db_host']
     + "' password='" + database_details['db_password'] + "'")
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
    """cursor = connection.cursor()
    cursor.execute("INSERT INTO tweets (tweet, subjectivity, polarity) VALUES (%s, %s, %s)",
                    (text, polarity, subjectivity))
    connection.commit()
    cursor.close()
    connection.close()"""

def commit_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except psycopg2.IntegrityError as e:
        pass

    connection.commit()
    cursor.close()

def store_user_information(tweet):
    #print(tweet)
    query = "INSERT INTO twitter_board_twitteruser (user_id, user_name, user_profile_image_url, user_verified, user_screen_name, user_followers) VALUES ('{0}', '{1}', '{2}', {3}, '{4}', {5})".format(tweet['user']['id'], tweet['user']['name'], tweet['user']['profile_image_url_https'], tweet['user']['verified'], tweet['user']['screen_name'], tweet['user']['followers_count'])
    commit_query(query)

def store_tweet_information(tweet, sentiment):
    #print(tweet)
    query = "INSERT INTO twitter_board_tweetdata (tweet_id, tweet, polarity, subjectivity, favourite_count, user_id) VALUES ('{0}', '{1}', {2}, {3}, {4}, '{5}')".format(tweet['id'], tweet['text'], sentiment.polarity, sentiment.subjectivity, tweet['favorite_count'], tweet['user']['id'])
    commit_query(query)

def filter_tweet(tweet):
    filtered = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", tweet['text']).split())
    filtered = filtered.replace("'", "")
    printable = set(string.printable)
    filtered = ''.join(filter(lambda x: x in printable, filtered))
    tweet['text'] = filtered
    print(filtered)

def analyze_and_store_data(tweet):
    filter_tweet(tweet)
    sentiment = TextBlob(tweet['text'])
    print(str(tweet['user']['id']) + ", " + tweet['user']['name'] + ", " + tweet['user']['profile_image_url_https']
        + ", " + str(tweet['user']['verified']) + ", " + tweet['user']['screen_name'] + ", " + str(tweet['user']['followers_count']))
    print(str(tweet['id']) + ", " + tweet['text'] + ", " + str(sentiment.polarity) + ", " + str(sentiment.subjectivity) + str(tweet['favorite_count']))
    print("\n")
    store_user_information(tweet)
    store_tweet_information(tweet, sentiment)

class StdOutListener(StreamListener):

    def __init__(self):
        self.COUNT = 0
        self.TOTAL = 3000

    def on_data(self, data):
        self.COUNT += 1
        if self.COUNT > self.TOTAL:
            return False
        data = json.loads(data)
        analyze_and_store_data(data)
        return True

    def on_error(self, status):
        print("Error with streaming")
        print(status)

#if __name__ == '__main__':

#This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(twitter_api['consumer_key'], twitter_api['consumer_secret'])
auth.set_access_token(twitter_api['access_token'], twitter_api['access_token_secret'])
stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['india'])