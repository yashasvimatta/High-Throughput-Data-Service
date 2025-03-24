from flask import Flask, request, jsonify
from constant.FieldNames import USER_ID_FIELD_NAME, USER_NAME_FIELD_NAME
from database.db import db
from exception.validation_exception import ValidationException
from models.rating import Rating
from models.movie import Movie
from models.user import User
from response.api_responses import APIResponse
from validator.create_user_request_validator import CreateUserRequestValidator

print("Starting Flask app")
app = Flask(__name__)

db()

@app.route("/", methods=["GET"])
def home():
    return APIResponse.ok_success('Application is live and healthy')

# Add user route
@app.route("/users", methods=["POST"])
def add_user():
    """
    Behavior:
     1. Adds a new user
     2. Throws error if the user_id exists
     3. Throws error if required attributes are not found

    Required attributes:
     1. user_id
     2. user_name
    """
    try:
        # Validate request
        CreateUserRequestValidator.validate(request)

        # Get payload
        payload = request.get_json()  
        if User.get_by_id(payload[USER_ID_FIELD_NAME]):
            return APIResponse.conflict('User already exists', 'RecordExistsException')

        # Create user
        new_user = User(user_id= payload[USER_ID_FIELD_NAME],
                        user_name = payload[USER_NAME_FIELD_NAME])
        new_user.save()
        return APIResponse.created('New User created')
    
    except ValidationException as ve:
        return ve.get_api_response()
    except Exception as e:
        return APIResponse.internal_server_error(str(e))


# Get user route
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        # Get user from db
        user = User.get_by_id(user_id)
        
        # Check if user exists
        if not user:
            return APIResponse.not_found('User not found')

        # Return user
        return APIResponse.ok_success(user)
    except Exception as e:
        return APIResponse.internal_server_error(str(e))
    
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
    