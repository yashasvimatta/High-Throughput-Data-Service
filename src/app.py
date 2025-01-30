from flask import Flask, request, redirect, jsonify
from database.db import db
from models.model import User, Movie, Rating

print("Starting Flask app")
app = Flask(__name__)

db()

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/add_rating", methods=["POST"])
def add_rating():
    try:
        data = request.get_json()
        required_data = ["user_id","movie_id","rating"]
        for i in required_data:
            if i not in data:
                return jsonify({"error": "Missing required fields"}), 400           # best practice to return jsonfied response and then the status code(bad request) is mentioned so it doesnt return 200

        new_rating =Rating(
            user_id=data["user_id"],
            movie_id=data["movie_id"],
            rating=float(data["rating"])
        )
        new_rating.save()
        return jsonify({"success": "Rating created successfully"}), 201 #201 Created is the standard HTTP status code for a successful POST request that results in the creation of a resource.
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/users/<int:user_id>",methods=["GET"])
def get_user_ratings(user_id):
    print(f"Received request for user_id: {user_id}")
    ratings = Rating.objects(user_id=user_id)
    response_lis = []
    for rating in ratings:
        response_lis.append({
            "movie_id": rating.movie_id,
            "rating": rating.rating,
            "timestamp": str(rating.timestamp) 
        })
    return jsonify(response_lis)

@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie_ratings_for_movieId(movie_id):
    ratings= Rating.objects(movie_id=movie_id)
    response_lis = []
    for rating in ratings:
        response_lis.append({
            "user_id": rating.user_id,
            "rating": rating.rating,
            "timestamp": str(rating.timestamp) 
        })
    return jsonify(response_lis)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    