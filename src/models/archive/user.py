from mongoengine import Document, IntField, FloatField, DateTimeField
class User(Document):
    user_id = IntField(required=True, unique=True)
