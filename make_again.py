from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import pandas as pd
from nltk.corpus import stopwords
import nltk
from math import log

FILENAME = 'text_emotion.csv'
class NaiveBayes(object):

    def __init__(self):
        self.classes = [
                'anger',
                'boredom',
                'empty',
                'enthusiasm',
                'fun',
                'happiness',
                'hate',
                'love',
                'neutral',
                'relief',
                'sadness',
                'surprise',
                'worry'
                ]
    def train(self, csv_file):
        raw_data = pd.read_csv(csv_file)
        # data is a pandas DataFrame
        data = {}
        for cat in self.classes:
            data[cat] = raw_data[raw_data['sentiment'] == cat]


        # data_pos = data[data['class'] == 'Pos']
        # data_neg = data[data['class'] == 'Neg']

        # positive_words = []
        # negative_words = []
        cat_words = {}

        # for text in data_pos['text']:
            # sentences = sent_tokenize(text)
            # for sentence in sentences:
                # words = word_tokenize(sentence)
                # positive_words.extend(words)
        # for text in data_neg['text']:
            # sentences = sent_tokenize(text)
            # for sentence in sentences:
                # words = word_tokenize(sentence)
                # negative_words.extend(words)
        for sentiment in self.classes:
            for text in data[sentiment]['content']:
                sentences = sent_tokenize(text)
                for sentence in sentences:
                    words = word_tokenize(sentence)
                    if sentiment in cat_words:
                        cat_words[sentiment].extend(words)
                    else:
                        cat_words[sentiment] = []
                        cat_words[sentiment].extend(words)


        stop_words = set(nltk.corpus.stopwords.words('english'))
        # filtered_pos = [w for w in positive_words if w not in stop_words]
        # filtered_neg = [w for w in negative_words if w not in stop_words]
        for sentiment in self.classes:
            cat_words[sentiment] = [w for w in cat_words[sentiment] if w not in stop_words]
            cat_words[sentiment] = [w.lower() for w in cat_words[sentiment]]

        self.sentimentCount = {}

        #Counters
        # self.positiveCount = Counter(filtered_pos)
        # self.negativeCount = Counter(filtered_neg)
        for sentiment in self.classes:
            self.sentimentCount[sentiment] = Counter(cat_words[sentiment])

        print("HERE")
        self.totalProbs = {}
        total_sum = 0
        total_counts = {}
        for sentiment in self.classes:
            total_counts[sentiment] = len(cat_words[sentiment])
            total_sum += total_counts[sentiment]

        # total_positive_words = len(positive_words)
        # total_negative_words = len(negative_words)
        # total_words = total_negative_words + total_positive_words
        for sentiment in self.classes:
            self.totalProbs[sentiment] = total_counts[sentiment]/total_sum

        # self.total_positive_prob = total_positive_words/total_words
        # self.total_negative_prob = total_negative_words/total_words
        for sentiment in self.classes:
            for word in self.sentimentCount[sentiment]:
                self.sentimentCount[sentiment][word] = self.sentimentCount[sentiment][word]/total_counts[sentiment]
        self.totalProbs['worry'] = self.totalProbs['worry']/2
        print(self.sentimentCount)
        print(self.totalProbs)

        # for key in self.positiveCount:
            # self.positiveCount[key] = self.positiveCount[key]/total_positive_words
        # for key in self.negativeCount:
            # self.negativeCount[key] = self.negativeCount[key]/total_negative_words


    def test(self, text):
        sentences = sent_tokenize(text)
        allwords = list()
        for sentence in sentences:
            words = word_tokenize(sentence)
            allwords.extend(words)
        stop_words = set(stopwords.words('english'))
        allwords = [word for word in allwords if word not in stop_words]
        allwords = [word.lower() for word in allwords]
        wordBayes = self.totalProbs
        for word in allwords:
            # pos_class = self.total_positive_prob
            # neg_class = self.total_negative_prob
            for sentiment in self.classes:
                if self.sentimentCount[sentiment].get(word):
                    wordBayes[sentiment] += self.sentimentCount[sentiment][word]

            max_sentiment = max(wordBayes.values())
            for sentiment in self.classes:
                if(wordBayes[sentiment] == max_sentiment):
                    print(sentiment)
                    break
            # if self.positiveCount.get(word):
                # pos_class += log(self.positiveCount[word])
                # print("Positive Word {}".format(word))

            # if self.negativeCount.get(word):
                # neg_class += log(self.negativeCount[word])
                # print("Negative Word {}".format(word))

        # print("Positive: {}, Negative: {}".format(pos_class, neg_class))

        # if(pos_class > neg_class):
            # print("Positive Sentiment")
        # else:
            # print("Negative Sentiment")

