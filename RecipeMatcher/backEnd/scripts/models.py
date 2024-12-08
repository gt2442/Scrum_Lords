from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    idUsers = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    passwordHash = db.Column(db.String(255), nullable=True)  
    current_diet = db.Column(db.String(50), nullable=True)  
    googleId = db.Column(db.String(255), nullable=True) 

    def set_password(self, password):
        """Hash and set the user's password."""
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the provided password against the hashed password."""
        return check_password_hash(self.passwordHash, password)

    def as_dict(self):
        """Convert the user object to a dictionary for JSON responses."""
        return {"id": self.idUsers, "username": self.username, "email": self.email}
