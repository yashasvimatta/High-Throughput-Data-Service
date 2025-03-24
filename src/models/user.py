from mongoengine import Document, IntField, StringField

class User(Document):
    user_id = IntField(required=True, unique=True, primary_key=True)
    user_name = StringField(required=True, unique=False)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.with_id(id)
