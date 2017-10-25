from math import sqrt


class NetflixModel:
    def __init__(self, cache, k):
        self.__cache = cache
        self.__k = k

    def __correlationCoefficient(self, activeUser, user):
        x, y, z = 0, 0, 0
        movies = self.__cache.getMoviesInCommon(activeUser, user)
        for movie in movies:
            a = self.__deltaRating(activeUser, movie)
            b = self.__deltaRating(user, movie)
            x += a * b
            y += a ** 2
            z += b ** 2

        return float(x) / sqrt(y * z)

    def __deltaRating(self, user, movie):
        return self.__cache.getRating(user, movie) - self.__cache.getMeanRating(user)

    def predictRating(self, activeUser, movie):
        x = 0
        allUsers = self.__cache.getAllUsers()
        for user in allUsers:
            if user != activeUser:
                x += self.__correlationCoefficient(activeUser, user) * self.__deltaRating(user, movie)

        return self.__cache.getMeanRating(activeUser) + self.__k * x
