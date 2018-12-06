import tweepy
from textblob import *
import time

consumer_key = 'GJY1UTiZ51QLI4k4ERBLlPCe8'
consumer_secret = 'vIDhLK72XHxaBrf3UY7lGEXnwq4yr2Px1Kmn3X8FgjpB22Xgup'

access_token = '980146058264227840-iLBkN3HTJplvpym7TVVrLCZLZpD1xUa'
access_token_secret = 'yEcyRtfBa1PP11IwZVtdUPG5j8AKCDy5k5w8DW52isnLq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

pol = [0]
sub = [0]
polAvg = 0
subAvg = 0

def getSentiment(term):
    public_tweets = api.search(term)
    i = 0
    global pol
    global sub
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        pol.append(analysis.sentiment.polarity)
        sub.append(analysis.sentiment.subjectivity)
    polAvg = sum(pol) / (len(pol)-1)
    subAvg = sum(sub) / (len(sub)-1)

def printSent(term):
    print(" *** ANALYZING TWEETS *** ")
    time.sleep(2)
    print(" *** CRUNCHING DATA *** ")
    time.sleep(2)
    getSentiment(term)
    print("")
    print("Average polarity: " + polAvg
    print("Average subjectivity: " + subAvg)
    print("")

def main():
    term = input("Enter search term: ")
    if not term == "quit":
        printSent(term)
    else:
        quit()
    main()

main()
