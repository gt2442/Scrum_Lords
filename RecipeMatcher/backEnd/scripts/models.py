from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    idUsers = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    passwordHash = db.Column(db.String(255), nullable=False)
    current_diet = db.Column(db.String(50), nullable=False)
    googleId = db.Column(db.String(255), nullable=False)


    def as_dict(self):
        return {"id": self.idUsers, "username": self.username, "email": self.email}
