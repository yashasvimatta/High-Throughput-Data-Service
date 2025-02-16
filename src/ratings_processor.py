import csv
from typing import List, Dict
from models.rating import Rating
from models.movie import Movie
from models.user import User
from database.db import db
from mongoengine.errors import DoesNotExist
from datetime import datetime
import requests

FLASK_APP_URL = "http://localhost:5000/add_rating"

class RatingsProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ratings = []

    def load_data(self):
        
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                payload={
                    "user_id": int(row['userId']),
                    "movie_id": int(row['movieId']),
                    "rating": float(row['rating'])
                }
                try:
                    response = requests.post(FLASK_APP_URL, json=payload)
                    if(response.status_code == 201):
                        print("Object created successfuly")
                    else:
                        print('Failed to add')         # user object with that specific userId is saved is retrived
                except requests.exceptions.RequestException as e:                                       #if that user doesnt exist then it is created
                    print(f"Error creating object: {e}")             


    def get_user_ratings(self, user_id: int) -> List[Rating]:
        return Rating.objects(user_id=user_id)


    def get_movie_ratings_for_movieId(self, movie_id: int):
        return Rating.objects(movie_id=movie_id)
    
    # avg rating of movie
    
if __name__ == "__main__":
    db()        # connect db
    processor = RatingsProcessor("../archive/ratings_small.csv")
    processor.load_data()