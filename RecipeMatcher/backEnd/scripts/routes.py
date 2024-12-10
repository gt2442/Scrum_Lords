from flask import Blueprint, jsonify, request, url_for
from .models import User, db
from authlib.integrations.flask_client import OAuth
import os

main_routes = Blueprint('main_routes', __name__)

# OAuth Configuration
oauth = OAuth()

# Define the Google OAuth configuration
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    client_kwargs={
        'scope': 'email profile',
    },
)

# Route: Get all users
@main_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])

# Route: Authenticate user
@main_routes.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):  # Secure password check
        return jsonify({
            "id": user.idUsers,
            "username": user.username,
            "email": user.email,
            "message": f"Welcome, {user.username}!"
        }), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Route: Add user
@main_routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'All fields are required: username, email, password'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 409
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)  # Hash password
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f"User '{username}' added successfully!"}), 201

# Route: Google OAuth login
@main_routes.route('/login/google')
def google_login():
    redirect_uri = url_for('main_routes.google_authorized', _external=True)
    return google.authorize_redirect(redirect_uri)

# Route: Google OAuth authorized callback
@main_routes.route('/login/google/authorized')
def google_authorized():
    token = google.authorize_access_token()  # Fetch the token
    user_info = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()

    email = user_info['email']
    google_id = user_info['id']

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, googleId=google_id)
        db.session.add(user)
        db.session.commit()

    return jsonify({
        "id": user.idUsers,
        "username": user.username,
        "email": user.email,
        "message": f"Logged in as {user.username} via Google."
    })

@main_routes.route('/current-user', methods=['GET'])
def current_user():
    """Retrieve the logged-in user's state."""
    # Here you would integrate session or token management
    from flask import session  # Example: Session management
    user = session.get('user')  # Replace with your session or token logic
    if not user:
        return jsonify({"error": "No user is logged in."}), 401
    return jsonify(user)


