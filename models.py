from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    progress = db.relationship('UserProgress', backref='user', lazy=True)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_cn = db.Column(db.String(100), nullable=False)  # Chinese title
    title_en = db.Column(db.String(100), nullable=False)  # English title
    position_x = db.Column(db.Float, nullable=False)
    position_y = db.Column(db.Float, nullable=False)
    prerequisites = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=False)
    
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    status = db.Column(db.String(20))
    completed_at = db.Column(db.DateTime) 