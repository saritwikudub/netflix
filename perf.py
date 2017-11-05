import datetime


def start():
    return datetime.datetime.now()


def elapsedTime(startTime):
    timeDelta = (datetime.datetime.now() - startTime)
    ms = str(timeDelta.microseconds / 1000) + ' ms'
    if timeDelta.seconds < 1:
        return ms
    else:
        return str(timeDelta.seconds) + ' seconds & ' + ms
