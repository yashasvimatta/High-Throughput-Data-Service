from mongoengine import connect
import os
def db():
    try:
        # user = os.getenv("MONGO_USER", "admin")
        # password = os.getenv("MONGO_PASSWORD", "password")
        uri = os.getenv("MONGO_URI", "mongodb://mongo-service:27017/Ratings")

        connect(
            host=uri
        )
        print("Connected to database:", os.getenv("MONGO_DB_NAME"))
    except Exception as e:
        print(f"Database connection failed: {e}")
