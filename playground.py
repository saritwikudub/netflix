from NetflixCache import NetflixCache
from perf import start, end

test_data_file = "Data/TestingRatings.txt"
training_data_file = "Data/TrainingRatings.txt"

startTime = start()
testCache = NetflixCache(test_data_file)
print "total loading test cache took: " + end(startTime)

startTime = start()
trainingCache = NetflixCache(training_data_file)
print "total loading test cache took: " + end(startTime)
