from datetime import datetime
from mongoengine import Document, IntField, FloatField, DateTimeField

class Rating(Document):
    user_id = IntField(required=True)
    movie_id = IntField(required=True)
    rating = FloatField(required=True)
    timestamp = DateTimeField(default=datetime.now)
    # meta = {'collection': 'rating'}

