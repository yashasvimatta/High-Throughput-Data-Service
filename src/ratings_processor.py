import csv
from typing import List, Dict
from src.models.model import User, Movie, Rating
from src.database.db import db
from mongoengine.errors import DoesNotExist
from datetime import datetime

class RatingsProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ratings = []

    def load_data(self):
        
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    user = User.objects.get(user_id=int(row['userId']))         # user object with that specific userId is saved is retrived
                except User.DoesNotExist:                                       #if that user doesnt exist then it is created
                    user = User(user_id=int(row['userId']))  
                    user.save()             

                try:
                    movie = Movie.objects.get(movie_id=int(row['movieId']))
                except Movie.DoesNotExist:
                    movie = Movie(movie_id=int(row['movieId']))  
                    movie.save() 

                rating = Rating(
                    user_id=user.user_id,
                    movie_id=movie.movie_id,
                    rating=float(row['rating']),
                    timestamp=datetime.fromtimestamp(int(row['timestamp']))
                )
                rating.save()
                self.ratings.append(rating)

    def get_user_ratings(self, user_id: int) -> List[Rating]:
        return Rating.objects(user_id=user_id)


    def get_movie_ratings_for_movieId(self, movie_id: int):
        return Rating.objects(movie_id=movie_id)
    
    # avg rating of movie
    
if __name__ == "__main__":
    db()        # connect db
    
    processor = RatingsProcessor("/app/archive/ratings_small.csv")
    processor.load_data()

    user_ratings = processor.get_user_ratings(1)
    print(f"User 1 has {len(user_ratings)} ratings.")       #  get ratings for user 1
    for rating in user_ratings:
        print(f"User {rating.user_id} rated Movie {rating.movie_id} with {rating.rating} stars")

    movie_ratings = processor.get_movie_ratings_for_movieId(31)
    print(f"Movie 31 has {len(movie_ratings)} ratings.")
    for rating in movie_ratings:
        print(f"User {rating.user_id} rated Movie {rating.movie_id} with {rating.rating} stars")         # get ratings by movieid
