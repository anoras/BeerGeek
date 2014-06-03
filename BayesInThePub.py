import pprint
import nltk

pos_reviews = [
    ("Absolutely fantastic, smooth as silk", 'positive'),
    ("I love this beer", 'positive'),
    ("This tastes great", 'positive'),
    ("Perfection", 'positive'),
    ("I'm so excited about this beer", 'positive'),
    ("This might just be the best beer ever", 'positive')
]

neg_reviews = [
    ("Absolutely horrible, harsh as yuck", 'negative'),
    ("I do not like this beer", 'negative'),
    ("This beer tastes terrible", 'negative'),
    ("Lame", 'negative'),
    ("I'm not at all excited about this beer", 'negative'),
    ("This might just be the worst beer ever", 'negative')
]

reviews = []
for (words, sentiment) in pos_reviews + neg_reviews:
    words_filtered = [word.lower() for word in words.split() if len(word) >= 3]
    reviews.append((words_filtered, sentiment))

print pprint.pformat(reviews,3)

def get_words_in_reviews(reviews):
    all_words = []
    for (words, sentiment) in reviews:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_reviews(reviews))

print pprint.pformat(word_features,3)

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, reviews)

print pprint.pformat(training_set,3)

classifier = nltk.NaiveBayesClassifier.train(training_set)
print classifier.show_most_informative_features(32)

print classifier.classify(extract_features("I'm super excited about this beer".split()))
print classifier.classify(extract_features("This beer tastes yuck".split()))
print classifier.classify(extract_features("This beer tastes bad".split()))