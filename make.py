from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import pandas as pd
from nltk.corpus import stopwords
import nltk
from math import log

FILENAME = 'movie-pang02.csv'
class NaiveBayes(object):

    def train(self, csv_file):
        data = pd.read_csv(csv_file)
        # data is a pandas DataFrame

        data_pos = data[data['class'] == 'Pos']
        data_neg = data[data['class'] == 'Neg']

        positive_words = []
        negative_words = []

        for text in data_pos['text']:
            sentences = sent_tokenize(text)
            for sentence in sentences:
                words = word_tokenize(sentence)
                positive_words.extend(words)
        for text in data_neg['text']:
            sentences = sent_tokenize(text)
            for sentence in sentences:
                words = word_tokenize(sentence)
                negative_words.extend(words)

        stop_words = set(nltk.corpus.stopwords.words('english'))
        filtered_pos = [w for w in positive_words if w not in stop_words]
        filtered_neg = [w for w in negative_words if w not in stop_words]

        #Counters
        self.positiveCount = Counter(filtered_pos)
        self.negativeCount = Counter(filtered_neg)

        total_positive_words = len(positive_words)
        total_negative_words = len(negative_words)
        total_words = total_negative_words + total_positive_words
        self.total_positive_prob = total_positive_words/total_words
        self.total_negative_prob = total_negative_words/total_words

        for key in self.positiveCount:
            self.positiveCount[key] = self.positiveCount[key]/total_positive_words
        for key in self.negativeCount:
            self.negativeCount[key] = self.negativeCount[key]/total_negative_words


    def test(self, text):
        sentences = sent_tokenize(text)
        allwords = list()
        for sentence in sentences:
            words = word_tokenize(sentence)
            allwords.extend(words)
        stop_words = set(stopwords.words('english'))
        allwords = [word for word in allwords if word not in stop_words]
        for word in allwords:
            pos_class = self.total_positive_prob
            neg_class = self.total_negative_prob
            if self.positiveCount.get(word):
                pos_class += log(self.positiveCount[word])
                print("Positive Word {}".format(word))

            if self.negativeCount.get(word):
                neg_class += log(self.negativeCount[word])
                print("Negative Word {}".format(word))

        print("Positive: {}, Negative: {}".format(pos_class, neg_class))

        if(pos_class > neg_class):
            print("Positive Sentiment")
        else:
            print("Negative Sentiment")

