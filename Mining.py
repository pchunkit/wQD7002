import tweepy
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time
import snscrape.modules.twitter as sntwitter
import csv


consumer_key = 'iRIRZsG0sqWptNMMNFZLH8v4I'
consumer_secret = 'l1MaSejTI52BKFBEYdXrOg8rVez25NESj3NXphQezJlQpTWVkK'
access_token = '1155013638224089089-gebMBVOI0QsxxRbAP59vlVMNP8Zvhn'
access_token_secret = 'LbrJvDJSXSo9UNMht3CVCn9jFeLuUByGkhG7Q6JAJ4qhO'


# Authenticate to Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Initialise these variables:
csvFile = open('lockdown2021.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('"malaysia" (#lockdown)' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('MCO2021.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#mco' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('Movementcontrolorder2021.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('movement control order' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('pkp2021.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pkp' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('perintah2021.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Perintah Kawalan Pergerakan' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('perintah.csv', 'w', encoding='utf8')  #creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Perintah Kawalan Pergerakan' + ' ' + 'lang:en since:2021-03-16 until:2021-05-06 -filter:links -filter:retweets' ).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.content , tweet.place])  # If you need more information, just provide the attributes

csvFile = open('lockdown2020.csv', 'w', encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        '"malaysia" (#lockdown)' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes

csvFile = open('MCO2020.csv', 'w', encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        '#mco' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes

csvFile = open('Movementcontrolorder2020.csv', 'w',
               encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        'movement control order' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes

csvFile = open('pkp2020.csv', 'w', encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        'pkp' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes

csvFile = open('perintah2020.csv', 'w', encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        'Perintah Kawalan Pergerakan' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes

csvFile = open('perintah.csv', 'w', encoding='utf8')  # creates a file in which you want to store the data.
csvWriter = csv.writer(csvFile)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        'Perintah Kawalan Pergerakan' + ' ' + 'lang:en since:2020-03-16 until:2020-05-06 -filter:links -filter:retweets').get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow(
        [tweet.date, tweet.content, tweet.place])  # If you need more information, just provide the attributes