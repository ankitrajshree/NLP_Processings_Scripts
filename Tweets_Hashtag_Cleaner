# -*- coding: utf-8 -*-
import pandas as pd
import re
import codecs

basepath = '/home/local/ASUAD/arajshre/Hungary/TwitterData_Hungary/'
filename = 'standwithceu/standwithceu.csv'
df = pd.read_csv(basepath+filename)
htag_set = set()


def clean_tweets(tweet):
    tweet = re.sub(r'\n | [^A-Za-z0-9]', ' ', tweet)
    # Remove the retweet information
    tweet = re.sub(r'RT @\S+', '', tweet)
    # Remove hyperlinks from text
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'pic\S+', '', tweet)
    tweet = re.sub(r'#' , '',tweet)
    tweet = re.sub(r'@\S+', '', tweet)
    tweet = re.sub(r'\|', '', tweet)
    return tweet.strip()


def hashtag_cleaner(hashtag):
    htag = re.sub(r'http\S+', '', hashtag)
    htag = re.sub(r'#', '', hashtag)
    return htag


def get_hashtag_from_str(htag):
    # Remove http links
    htag = re.split('http|pic', htag)[0].strip()
    htag = re.sub(r'\n | [^A-Za-z0-9]', ' ', htag)
    htag_1 = htag.split(' ')
    # htag_set = set(htag_1)
    # htag_1 = re.sub(r'\n','',htag_1)
    # print'Htags : ',htag_1
    for htag in htag_1:
        htag_set.add(htag)


tweet_list = df['tweet_text'].tolist()
# hashtags = df['hashtag'].dropna().tolist()
# cleaned_hashtags = map(hashtag_cleaner, hashtags)
# map(get_hashtag_from_str, cleaned_hashtags)
clean_tweet_list = map(clean_tweets, tweet_list)
# print 'Tweet_list',clean_tweet_list
fw = codecs.open('Tweets.txt', 'a+')
for tweet in clean_tweet_list:
    if tweet != '':
        fw.write('%s\n' % tweet)
# with open('hashtags.txt', 'a+') as fw:
#     for ht in htag_set:
#         fw.write("%s\n" % ht)
# print 'Hashtags',cleaned_hashtags
