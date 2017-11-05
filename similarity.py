import math


# O(m)
def calc_pearsons_similarity(user1, user2, d_user_movies, d_ratings):
    if user1 == user2:
        return 0

    user1_movies = d_user_movies[user1]
    x = 0
    y = 0

    for idx, movie in enumerate(user1_movies):
        if (user2, movie) in d_ratings:
            d_rating1 = d_ratings[user1, movie]
            d_rating2 = d_ratings[user2, movie]
            x += d_rating1 * d_rating2
            y += math.pow(d_rating1, 2) * math.pow(d_rating2, 2)

    return 0 if y == 0 else float(x) / y
