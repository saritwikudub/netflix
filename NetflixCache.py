import io


class NetflixCache:
    def __init__(self, fileName):
        self.__ratingsCache = {}
        self.__meanRatingsCache = {}
        self.__load(fileName)

    def __load(self, fileName):
        data = io.loadRaw(fileName)
        count = {}

        for idx, row in enumerate(data):
            user, movie, rating = row['user'], row['movie'], row['rating']

            if user not in self.__ratingsCache:
                self.__ratingsCache[user] = {}
                self.__meanRatingsCache[user] = 0
                count[user] = 0

            count[user] += 1

            self.__ratingsCache[user][movie] = rating
            self.__meanRatingsCache[user] += rating

        for user in self.__meanRatingsCache.iterkeys():
            self.__meanRatingsCache[user] = float(self.__meanRatingsCache[user]) / count[user]

    def getMeanRating(self, user):
        return self.__meanRatingsCache[user]

    def getAllUsers(self):
        return self.__ratingsCache.keys()

    def getRating(self, user, movie):
        return self.__ratingsCache[user][movie]

    def getUserMovies(self, user):
        return self.__ratingsCache[user].keys()

    # todo: costly
    def getMoviesInCommon(self, user1, user2):
        return set(self.getUserMovies(user1)).intersection(self.getUserMovies(user2))
