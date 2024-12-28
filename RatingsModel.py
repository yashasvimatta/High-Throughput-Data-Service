from datetime import datetime

class User:
    def __init__(self, user_id):
        self.user_id = user_id


class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = datetime.fromtimestamp(timestamp)
