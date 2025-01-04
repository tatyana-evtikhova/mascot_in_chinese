from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from models import db, User, Lesson, UserProgress
import os
import markdown
import random
from forms import RegistrationForm, LoginForm
from functools import wraps
from flask import abort
from datetime import datetime
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinese_lessons.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a secure secret key
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Replace with your app password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

mail = Mail(app)

# Token serializer for secure tokens
def get_token_serializer():
    return URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Email sending functions
def send_verification_email(user):
    token = get_token_serializer().dumps(user.email, salt='email-verification')
    verify_url = url_for('verify_email', token=token, _external=True)
    
    msg = Message('Verify Your Email',
                 recipients=[user.email],
                 html=render_template('email/verify_email.html',
                                    verify_url=verify_url))
    mail.send(msg)
    user.email_verification_sent_at = datetime.utcnow()
    db.session.commit()

def send_password_reset_email(user):
    token = get_token_serializer().dumps(user.email, salt='password-reset')
    reset_url = url_for('reset_password', token=token, _external=True)
    
    msg = Message('Reset Your Password',
                 recipients=[user.email],
                 html=render_template('email/reset_password.html',
                                    reset_url=reset_url))
    mail.send(msg)

def send_welcome_email(user):
    msg = Message('Welcome to Mascot in Chinese!',
                 recipients=[user.email],
                 html=render_template('email/welcome.html',
                                    user=user))
    mail.send(msg)

def send_achievement_email(user, achievement, next_steps):
    msg = Message(f'New Achievement: {achievement["name"]}',
                 recipients=[user.email],
                 html=render_template('email/achievement.html',
                                    achievement=achievement,
                                    next_steps=next_steps))
    mail.send(msg)

def send_study_reminder(user):
    # Get user's progress data
    total_lessons = Lesson.query.count()
    completed_lessons = UserProgress.query.filter_by(
        user_id=user.id,
        status='completed'
    ).count()
    progress_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    
    # Get recommended next lesson
    recommended_lesson = Lesson.query.filter_by(is_active=True).first()
    
    msg = Message('Time for Your Daily Chinese Practice!',
                 recipients=[user.email],
                 html=render_template('email/study_reminder.html',
                                    user=user,
                                    streak_days=3,  # Replace with actual streak
                                    progress_percentage=progress_percentage,
                                    recommended_lesson=recommended_lesson))
    mail.send(msg)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def lesson_map():
    return render_template('lesson_map.html')

@app.route('/api/lessons')
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([{
        'id': lesson.id,
        'title': f"{lesson.title_cn}\n{lesson.title_en}",
        'position': {
            'x': lesson.position_x,
            'y': lesson.position_y
        },
        'prerequisites': [int(x) for x in lesson.prerequisites.split(',') if x],
        'is_active': lesson.is_active
    } for lesson in lessons])

@app.route('/api/progress/<int:user_id>')
def get_progress(user_id):
    progress = UserProgress.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'lesson_id': p.lesson_id,
        'status': p.status
    } for p in progress])

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    lessons = Lesson.query.all()
    
    try:
        lesson_module = __import__(f'lessons.lesson{lesson_id}', fromlist=['lesson'])
        lesson_data = lesson_module.lesson
        
        # Create a dictionary with all lesson attributes
        lesson_dict = {
            'id': lesson.id,
            'title': lesson_data['title'],  # Use title from lesson module
            'title_cn': lesson.title_cn,
            'title_en': lesson.title_en,
            'position_x': lesson.position_x,
            'position_y': lesson.position_y,
            'prerequisites': lesson.prerequisites,
            'is_active': lesson.is_active,
            'content': lesson_data['content']
        }
        
        from types import SimpleNamespace
        lesson = SimpleNamespace(**lesson_dict)
        
    except ImportError:
        # If lesson module not found, create empty content structure
        lesson.content = {
            'stages': [
                {
                    'name': 'Content Not Found',
                    'type': 'error',
                    'content': 'The lesson content could not be loaded.'
                }
            ],
            'tips': '<p>No study tips available for this lesson.</p>'
        }
    
    return render_template('lesson.html', 
                         lesson=lesson, 
                         lessons=lessons,
                         lesson_title=lesson.title)  # Pass the title to template

def init_db():
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Create admin user
        admin = User(
            email="admin@example.com",
            username="admin",
            is_active=True,
            is_admin=True
        )
        admin.set_password("admin123")  # You should use a more secure password
        
        # Create regular test user
        test_user = User(
            email="test@example.com",
            username="test_user",
            is_active=True,
            is_admin=False
        )
        test_user.set_password("test123")
        
        try:
            db.session.add(admin)
            db.session.add(test_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error creating users: {e}")

        if not Lesson.query.first():
            sample_lessons = [
                Lesson(
                    title_cn="基础问候",
                    title_en="Basic Greetings",
                    position_x=20,
                    position_y=30,
                    prerequisites="",
                    is_active=True
                ),
                Lesson(
                    title_cn="数字 1-10",
                    title_en="Numbers 1-10",
                    position_x=40,
                    position_y=25,
                    prerequisites="1",
                    is_active=False
                ),
                Lesson(
                    title_cn="家庭成员",
                    title_en="Family Members",
                    position_x=60,
                    position_y=35,
                    prerequisites="1",
                    is_active=False
                ),
                Lesson(
                    title_cn="颜色",
                    title_en="Colors",
                    position_x=35,
                    position_y=50,
                    prerequisites="1",
                    is_active=False
                ),
                Lesson(
                    title_cn="数字 11-100",
                    title_en="Numbers 11-100",
                    position_x=55,
                    position_y=45,
                    prerequisites="2",
                    is_active=False
                ),
                Lesson(
                    title_cn="日期和时间",
                    title_en="Date & Time",
                    position_x=75,
                    position_y=50,
                    prerequisites="2,5",
                    is_active=False
                ),
                Lesson(
                    title_cn="食物",
                    title_en="Food",
                    position_x=45,
                    position_y=65,
                    prerequisites="1,4",
                    is_active=False
                ),
                Lesson(
                    title_cn="购物",
                    title_en="Shopping",
                    position_x=65,
                    position_y=70,
                    prerequisites="5,7",
                    is_active=False
                ),
            ]
            for lesson in sample_lessons:
                db.session.add(lesson)
            db.session.commit()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))

        user = User(email=email, username=username)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            send_verification_email(user)
            send_welcome_email(user)
            login_user(user)
            flash('Registration successful! Please check your email to verify your account.', 'success')
            return redirect(url_for('lesson_map'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('register'))

    return render_template('auth/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('lesson_map'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user)
            flash('Logged in successfully.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('lesson_map'))
        flash('Invalid email or password', 'error')
    return render_template('auth/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('lesson_map'))

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    return render_template('admin/dashboard.html', users=users)

@app.route('/dashboard')
@login_required
def user_dashboard():
    # Calculate user progress
    total_lessons = Lesson.query.count()
    completed_lessons = UserProgress.query.filter_by(
        user_id=current_user.id,
        status='completed'
    ).count()
    
    progress_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    
    # Mock data for demonstration
    achievements = [
        {
            'icon': '🌟',
            'name': 'First Lesson',
            'description': 'Complete your first lesson',
            'unlocked': completed_lessons > 0
        },
        {
            'icon': '🔥',
            'name': '3-Day Streak',
            'description': 'Study for 3 days in a row',
            'unlocked': False
        }
    ]
    
    recent_activities = [
        {
            'icon': 'bi-book',
            'title': 'Completed Basic Greetings',
            'timestamp': datetime.now()
        }
    ]
    
    return render_template('user/dashboard.html',
                         progress_percentage=progress_percentage,
                         completed_lessons=completed_lessons,
                         streak_days=3,  # Mock data
                         total_time=12.5,  # Mock data
                         achievements=achievements,
                         recent_activities=recent_activities)

@app.route('/profile')
@login_required
def user_profile():
    # Get user progress data
    total_lessons = Lesson.query.count()
    completed_lessons = UserProgress.query.filter_by(
        user_id=current_user.id,
        status='completed'
    ).count()
    
    # Calculate progress percentage
    progress_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    
    # Get user rank
    users = User.query.all()
    users_sorted = sorted(users, key=lambda x: UserProgress.query.filter_by(
        user_id=x.id, status='completed').count(), reverse=True)
    rank = users_sorted.index(current_user) + 1
    
    # Get recent achievements (mock data for now)
    recent_achievements = [
        {
            'id': 1,
            'icon': '🌟',
            'name': 'First Lesson',
            'description': 'Completed your first lesson',
            'earned_at': datetime.utcnow()
        }
    ]
    
    # Get top users for leaderboard
    top_users = [{
        'id': user.id,
        'username': user.username,
        'points': UserProgress.query.filter_by(user_id=user.id, status='completed').count() * 10
    } for user in users_sorted[:5]]

    return render_template('user/profile.html',
                         completed_lessons=completed_lessons,
                         streak_days=3,  # Mock data for now
                         rank=rank,
                         progress_percentage=progress_percentage,
                         recent_achievements=recent_achievements,
                         top_users=top_users)

@app.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    username = request.form.get('username')
    email = request.form.get('email')
    
    if username != current_user.username:
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('user_profile'))
            
    if email != current_user.email:
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('user_profile'))
    
    current_user.username = username
    current_user.email = email
    db.session.commit()
    flash('Profile updated successfully', 'success')
    return redirect(url_for('user_profile'))

@app.route('/profile/password', methods=['POST'])
@login_required
def change_password():
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    if not current_user.check_password(current_password):
        flash('Current password is incorrect', 'error')
        return redirect(url_for('user_profile'))
        
    if new_password != confirm_password:
        flash('New passwords do not match', 'error')
        return redirect(url_for('user_profile'))
        
    current_user.set_password(new_password)
    db.session.commit()
    flash('Password changed successfully', 'success')
    return redirect(url_for('user_profile'))

@app.route('/profile/preferences', methods=['POST'])
@login_required
def update_preferences():
    current_user.daily_goal = request.form.get('daily_goal', type=int)
    current_user.difficulty = request.form.get('difficulty')
    current_user.show_pinyin = 'show_pinyin' in request.form
    
    db.session.commit()
    flash('Learning preferences updated successfully', 'success')
    return redirect(url_for('user_profile'))

@app.route('/profile/notifications', methods=['POST'])
@login_required
def update_notifications():
    current_user.daily_reminder = 'daily_reminder' in request.form
    current_user.achievement_notification = 'achievement_notification' in request.form
    current_user.email_updates = 'email_updates' in request.form
    
    db.session.commit()
    flash('Notification settings updated successfully', 'success')
    return redirect(url_for('user_profile'))

@app.route('/profile/delete', methods=['POST'])
@login_required
def delete_account():
    if request.form.get('confirm_delete') == current_user.email:
        # Delete user data
        UserProgress.query.filter_by(user_id=current_user.id).delete()
        db.session.delete(current_user)
        db.session.commit()
        logout_user()
        flash('Your account has been deleted', 'info')
        return redirect(url_for('lesson_map'))
    
    flash('Please confirm your email to delete account', 'error')
    return redirect(url_for('user_profile'))

@app.route('/verify-email/<token>')
def verify_email(token):
    try:
        email = get_token_serializer().loads(token, salt='email-verification', max_age=86400)  # 24 hours
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_verified = True
            db.session.commit()
            flash('Your email has been verified!', 'success')
        else:
            flash('Invalid verification link', 'error')
    except:
        flash('The verification link is invalid or has expired', 'error')
    return redirect(url_for('login'))

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            send_password_reset_email(user)
            flash('Password reset instructions have been sent to your email', 'info')
        else:
            flash('Email address not found', 'error')
        return redirect(url_for('login'))
    return render_template('auth/forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = get_token_serializer().loads(token, salt='password-reset', max_age=3600)  # 1 hour
        if request.method == 'POST':
            user = User.query.filter_by(email=email).first()
            if user:
                password = request.form.get('password')
                confirm_password = request.form.get('confirm_password')
                if password == confirm_password:
                    user.set_password(password)
                    db.session.commit()
                    flash('Your password has been reset!', 'success')
                    return redirect(url_for('login'))
                else:
                    flash('Passwords do not match', 'error')
            else:
                flash('Invalid reset link', 'error')
        return render_template('auth/reset_password.html')
    except:
        flash('The reset link is invalid or has expired', 'error')
        return redirect(url_for('forgot_password'))

def get_lesson_content(lesson_id):
    if lesson_id == 1:
        # Keep Lesson 1 exactly as is - it serves as our template
        return existing_lesson_1_content
    else:
        # Template structure for all other lessons
        return {
            "stages": [
                # Theory Section
                {
                    "type": "theory",
                    "name": "Basic Concepts",  # Change per lesson
                    "content": """
                        <div class="learning-section">
                            <div class="section-intro">
                                <p>Introduction text for the lesson...</p>
                            </div>
                            
                            <div class="main-expression">
                                <div class="expression-content">
                                    <div class="chinese-text">你好</div>
                                    <div class="expression-details">
                                        <div class="pinyin">nǐ hǎo</div>
                                        <div class="meaning">Hello</div>
                                    </div>
                                </div>
                            </div>

                            <div class="theory-content">
                                <p>Explanation of the concept...</p>
                            </div>
                        </div>
                    """
                },
                
                # Common Usage Section
                {
                    "type": "examples",
                    "name": "Common Usage",
                    "content": """
                        <div class="usage-examples">
                            <h4>Examples:</h4>
                            <div class="usage-item" onclick="speakText('Chinese text here')">
                                <div class="example-content">
                                    <div class="chinese-text">Chinese text</div>
                                    <div class="pinyin">Pinyin here</div>
                                    <div class="meaning">English meaning</div>
                                </div>
                            </div>
                            <!-- More usage examples... -->
                        </div>

                        <div class="usage-notes">
                            <h4>Usage Notes:</h4>
                            <ul>
                                <li>Note 1...</li>
                                <li>Note 2...</li>
                            </ul>
                        </div>
                    """
                }
            ],
            "tips": """
                <ul>
                    <li>Study tip 1...</li>
                    <li>Study tip 2...</li>
                    <li>Study tip 3...</li>
                </ul>
            """
        }

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True) 