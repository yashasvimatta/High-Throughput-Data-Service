from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def db():
    try:
        connect(
            db=os.getenv("MONGO_DB_NAME"),
            host=os.getenv("MONGO_URI")
        )
        print("Connected to database:", os.getenv("MONGO_DB_NAME"))
    except Exception as e:
        print(f"Database connection failed: {e}")
