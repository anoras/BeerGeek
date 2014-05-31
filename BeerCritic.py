# coding=utf-8
from collections import Counter
import json
import pickle
import random
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.punkt import PunktWordTokenizer
import numpy
import re
from termcolor import colored, cprint


with open('data/classification.pickle') as f:
    sentence_classifier = pickle.load(f)

with open('data/sentiments.pickle') as f:
    sentiment_classifier = pickle.load(f)

def extract_features(sentence):
    if not sentence: sentence = ""
    words = PunktWordTokenizer().tokenize(sentence)
    # part of speech tag each of the words
    pos = nltk.pos_tag(words)
    pos = [nltk.simplify_wsj_tag(tag) for word, tag in pos]
    words = [word.lower() for word in words]
    trigrams = nltk.trigrams(words)
    trigrams = ["%s/%s/%s" % (trigram[0], trigram[1], trigram[2]) for trigram in trigrams]
    features = words + pos + trigrams
    features = dict([(feature, True) for feature in features])
    return features


with open('data/beer-review-pages.json', 'r') as f:
    beer_review_pages = json.load(f)
    random.shuffle(beer_review_pages)
    for beer_review_page in beer_review_pages:
        with open('data/' + beer_review_page['filename'] + '.html','r') as html_file:
            cprint(beer_review_page['title'], 'cyan')
            html = BeautifulSoup(html_file)
            sentences = nltk.sent_tokenize(html.get_text())
            review_sentences = []
            for sentence in sentences:
                sentence = re.sub(u'\s+', ' ', sentence)
                features = extract_features(sentence)
                classification = sentence_classifier.classify(features)
                print classification + ": " + sentence
                if classification == 'review':
                    review_sentences.append(sentiment_classifier.classify(features))

            raw_input(Counter(numpy.array(review_sentences).flat).most_common(1))