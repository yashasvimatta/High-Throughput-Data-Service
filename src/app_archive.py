from flask import Flask, request, redirect, jsonify
from database.db import db
from models.rating import Rating
from models.movie import Movie
from models import User

print("Starting Flask app")
app = Flask(__name__)

db()

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

# Add user route
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user = request.get_json()
        required_data = ["user_id"]
        for i in required_data:
            if i not in user:
                return jsonify({"error": "Missing user id"}), 400
            
        if User.objects(user_id=user["user_id"]).first():
            return jsonify({"message": "User already exists"}), 200          # user already exists
        
        new_user = User(user_id= user["user_id"])
        new_user.save()
        return jsonify({"success": "New User created"}), 201
    except Exception as e:
        return jsonify({"error":str(e)}), 500


# Get user route
@app.route("/get_user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = User.objects(user_id=user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"user_id":user.user_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Add movie route
@app.route("/add_movie", methods=["POST"])
def add_movie():
    try:
        movie = request.get_json()
        required_data = ["movie_id"]
        for i in required_data:
            if i not in movie:
                return jsonify({"error": "Missing movie id"}), 400
            
        if Movie.objects(movie_id=movie["movie_id"]).first():
            return jsonify({"message":"Movie already exists"}), 200
        new_movie = Movie(movie_id= movie["movie_id"])
        new_movie.save()
        return jsonify({"success": "New movie created"}), 201
    except Exception as e:
        return jsonify({"error":str(e)}), 500

# Get movie route   
@app.route("/get_movie/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    try:
        movie = Movie.objects(movie_id=movie_id).first()
        if not movie:
            return jsonify({"error": "Movie not found"}), 404
        return jsonify({"movie_id":movie.movie_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add rating route 
@app.route("/add_rating", methods=["POST"])
def add_rating():
    try:
        data = request.get_json()
        required_data = ["user_id","movie_id","rating"]
        for i in required_data:
            if i not in data:
                return jsonify({"error": "Missing required fields"}), 400   # best practice to return jsonfied response and then the status code(bad request) is mentioned so it doesnt return 200

        new_rating =Rating(
            user_id=data["user_id"],
            movie_id=data["movie_id"],
            rating=float(data["rating"])
        )
        new_rating.save()
        return jsonify({"success": "Rating created successfully"}), 201 #201 Created is the standard HTTP status code for a successful POST request that results in the creation of a resource.
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get rating by user id
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

# Get ratings by movie id
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
    