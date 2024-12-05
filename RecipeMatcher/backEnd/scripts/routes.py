from flask import Blueprint, jsonify, request
from .models import User, db

main_routes = Blueprint('main_routes', __name__)
app = Blueprint('app', __name__)

# Route to get all users
@main_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])

# Authentication route
@main_routes.route('/auth', methods=['POST'])
def authenticate_user():
    # Get JSON data from the request
    data = request.get_json()
    username = data.get('username').strip()  # Remove any leading/trailing whitespace
    password = data.get('password').strip()  # Remove any leading/trailing whitespace
    
    # Validate that both username and password are provided
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Debug: Log the values being used for the query
    print(f"Attempting authentication for username: '{username}' with password: '{password}'")

    # Query the database to check if user exists with provided credentials
    user = User.query.filter_by(username=username, password=password).first()

    # Debug: Check if the query returned a user
    if user:
        print(f"Authentication successful for username: '{username}'")
        return jsonify({"message": f"Welcome, {username}!"}), 200
    else:
        print(f"Authentication failed for username: '{username}'")
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/users', methods=['POST'])
def add_user():
    """Handle POST requests to add a new user."""
    try:
        # Get JSON data from the request
        data = request.get_json()
 
        # Validate the required fields
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')  # You should hash this password for security
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required: username, email, password'}), 400
 
        # Check if the username or email already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 409
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 409
 
        # Add the user to the database
        new_user = User(username=username, email=email, passwordHash=password)  # Hashing recommended
        db.session.add(new_user)
        db.session.commit()
 
        return jsonify({'message': f"User '{username}' added successfully!"}), 201
 
    except Exception as e:
        return jsonify({'error': str(e)}), 500