# coding=utf-8
import json
import random
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.punkt import PunktWordTokenizer
import re
from termcolor import colored, cprint

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



with open('data/classification-training.json','r') as f:
    classification_training = json.load(f)

with open('data/sentiment-training.json','r') as f:
    sentiment_training = json.load(f)


def save_classifcations():
    with open('data/classification-training.json','wb') as f:
        json.dump(classification_training,f)

    with open('data/sentiment-training.json','wb') as f:
        json.dump(sentiment_training,f)


with open('data/beer-review-pages.json', 'r') as f:
    beer_review_pages = json.load(f)
    random.shuffle(beer_review_pages)
    for beer_review_page in beer_review_pages:
        with open('data/' + beer_review_page['filename'] + '.html','r') as html_file:
            cprint(beer_review_page['title'], 'cyan')
            html = BeautifulSoup(html_file)
            sentences = nltk.sent_tokenize(html.get_text())
            classifications = []
            for sentence in sentences:
                sentence = re.sub(u'\s+', ' ', sentence)
                features = extract_features(sentence)
                sentence_kind = raw_input(sentence)
                if sentence_kind == 'r':
                    classifications.append((features, 'review'))
                    classification_training.append((features, 'review'))
                elif sentence_kind == 'd':
                    classifications.append((features, 'description'))
                    classification_training.append((features, 'description'))
                elif sentence_kind == 'o':
                    classifications.append((features, 'other'))
                    classification_training.append((features, 'other'))
                elif sentence_kind == 'q':
                    save_classifcations()
                    exit()
                else:
                    pass

            review = raw_input(colored("Was this review positive (+), negative (-) or netural (n)? Or should I skip it (s)?", color='yellow'))
            review_sentiment = ""
            if review == '+':
                review_sentiment = "positive"
            elif review == '-':
                review_sentiment = "negative"
            elif review == 'n':
                review_sentiment = "neutral"
            elif review == 's':
                pass
            elif sentence_kind == 'q':
                save_classifcations()
                exit()

            for classification in classifications:
                if classification[1] == 'review':
                    print "Adding sent: " + review_sentiment
                    print classification[0]
                    sentiment_training.append((classification[0], review_sentiment))


    save_classifcations()