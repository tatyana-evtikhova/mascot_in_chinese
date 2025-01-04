from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    email_verified = db.Column(db.Boolean, default=False)
    email_verification_sent_at = db.Column(db.DateTime)
    progress = db.relationship('UserProgress', backref='user', lazy=True)
    daily_goal = db.Column(db.Integer, default=30)
    difficulty = db.Column(db.String(20), default='beginner')
    show_pinyin = db.Column(db.Boolean, default=True)
    daily_reminder = db.Column(db.Boolean, default=True)
    achievement_notification = db.Column(db.Boolean, default=True)
    email_updates = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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