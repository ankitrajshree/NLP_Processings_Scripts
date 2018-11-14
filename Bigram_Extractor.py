# -*- coding: utf-8 -*-
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import codecs

bigram_set = set()


def process_bigrams(text):
    tokens = text.split()
    ngram = ngrams(tokens,2)
    for i in ngram:
        print(i)
        bigram_set.add(i)


tweets = codecs.open('Tweets.txt', 'r').readlines()
map(process_bigrams, tweets)
with open('Bigrams.txt', 'w') as fw:
    for bigram in bigram_set:
        print('Bigram is : ',bigram)
        fw.write('%s\n' % str(bigram))