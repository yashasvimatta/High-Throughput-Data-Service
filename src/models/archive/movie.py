from mongoengine import Document, IntField, FloatField, DateTimeField
class Movie(Document):
    movie_id = IntField(required=True, unique=True)