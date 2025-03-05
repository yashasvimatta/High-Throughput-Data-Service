from mongoengine import connect
import os
def db():
    try:
        # user = os.getenv("MONGO_USER", "admin")
        # password = os.getenv("MONGO_PASSWORD", "password")
        host = os.getenv("MONGO_URI", "mongo-service")
        db_name = os.getenv("MONGO_DB_NAME", "Ratings")
        uri = f"mongodb://{host}:27017/{db_name}"

        connect(
            host=uri
        )
        print("Connected to database:", os.getenv("MONGO_DB_NAME"))
    except Exception as e:
        print(f"Database connection failed: {e}")
