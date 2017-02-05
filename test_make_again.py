from make_again import NaiveBayes

FILENAME = 'text_emotion.csv'

classifier = NaiveBayes()
classifier.train(FILENAME)



