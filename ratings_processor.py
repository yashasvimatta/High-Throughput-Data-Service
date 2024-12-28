import csv
from typing import List, Dict
from RatingsModel import User, Movie, Rating
from collections import defaultdict
class RatingsProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.users = defaultdict(User)
        self.movies = defaultdict(Movie)
        self.ratings = []

    def load_data(self):
        
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = int(row['userId'])
                if user_id not in self.users:       # check if user present otherwise create a new user object
                    self.users[user_id] = User(user_id)
                
                movie_id = int(row['movieId'])
                if movie_id not in self.movies:     # check if movie present otherwise create a new movie object
                    self.movies[movie_id] = Movie(movie_id)

                rating = Rating(
                    user_id=user_id,
                    movie_id=movie_id,
                    rating=float(row['rating']),
                    timestamp=int(row['timestamp'])
                )
                self.ratings.append(rating)

    def get_user_ratings(self, user_id: int) -> List[Rating]:
        user_ratings = []
        for rating in self.ratings:
            if rating.user_id == user_id:
                user_ratings.append(rating)
        return user_ratings


    def get_movie_ratings_for_movieId(self, movie_id: int):
        # movie_ratings = []
        # for rating in self.ratings:         # for each in ratings list 
        #     if rating.movie_id == movie_id:     # if movies 
        #         movie_ratings.append(rating)
        print(filter(lambda x: x.movie_id == movie_id, self.ratings))
        return list(filter(lambda x: x.movie_id == movie_id, self.ratings))
    
    
if __name__ == "__main__":
    processor = RatingsProcessor("archive/ratings_small.csv")
    processor.load_data()

    user_ratings = processor.get_user_ratings(1)
    print(f"User 1 has {len(user_ratings)} ratings.")       #  get ratings for user 1

    movie_ratings = processor.get_movie_ratings_for_movieId(31)
    print(f"Movie 31 has {len(movie_ratings)} ratings.")            #get ratings for movie 31

    for rating in movie_ratings:
        print(f"User {rating.user_id} rated Movie {rating.movie_id} with {rating.rating} stars")            # get ratings by movieid
