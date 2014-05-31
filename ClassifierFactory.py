# coding=utf-8
import pickle
import json
from nltk.classify import MaxentClassifier


if raw_input("Do you want to create a sentence classifier? [Y/n]") != 'n':
    with open('data/classification-training.json','r') as f:
        classification_training = json.load(f)
        classifier = MaxentClassifier.train(classification_training)
        with open("data/classification.pickle",'wb') as outfile:
            pickle.dump(classifier,outfile)

if raw_input("Do you want to create a sentiment classifier? [Y/n]") != 'n':
    with open('data/sentiment-training.json','r') as f:
        sentiment_training = json.load(f)
        classifier = MaxentClassifier.train(sentiment_training)
        with open("data/sentiments.pickle",'wb') as outfile:
            pickle.dump(classifier,outfile)