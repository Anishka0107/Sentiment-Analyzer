from make import NaiveBayes

FILENAME = 'movie-pang02.csv'

classifier = NaiveBayes()
classifier.train(FILENAME)



