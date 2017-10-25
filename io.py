import pickle

import numpy as np

import perf

data_type = np.dtype([('movie', np.int), ('user', np.int), ('rating', float)])


def persistObject(obj, fileName):
    fileHandler = open(fileName, 'w')
    pickle.dump(obj, fileHandler)


def loadObject(fileName):
    fileHandler = open(fileName, 'r')
    return pickle.load(fileHandler)


def loadRaw(fileName):
    startTime = perf.start()

    data = np.loadtxt(fname=fileName,
                      delimiter=',',
                      dtype=data_type)

    print "file: " + fileName + " , load time: " + perf.end(startTime)
    return data
