from flask import Flask, jsonify, render_template
from models import db, User, Lesson, UserProgress
import os
import markdown
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinese_lessons.db'
db.init_app(app)

def load_lesson_content(lesson_id):
    """Load lesson content from markdown files in the lessons directory"""
    lesson_path = os.path.join('lessons', str(lesson_id))
    print(f"Looking for lesson content in: {lesson_path}")  # Debug print
    
    content = {
        'theory': '',
        'practice': ''
    }
    
    # Load theory content
    theory_path = os.path.join(lesson_path, 'theory.md')
    print(f"Theory path: {theory_path}")  # Debug print
    print(f"Theory file exists: {os.path.exists(theory_path)}")  # Debug print
    
    if os.path.exists(theory_path):
        with open(theory_path, 'r', encoding='utf-8') as f:
            content['theory'] = markdown.markdown(f.read())
            print("Theory content loaded successfully")  # Debug print
            
    # Load practice content
    practice_path = os.path.join(lesson_path, 'practice.md')
    print(f"Practice path: {practice_path}")  # Debug print
    print(f"Practice file exists: {os.path.exists(practice_path)}")  # Debug print
    
    if os.path.exists(practice_path):
        with open(practice_path, 'r', encoding='utf-8') as f:
            content['practice'] = markdown.markdown(f.read())
            print("Practice content loaded successfully")  # Debug print
            
    return content

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
        db.create_all()
        # Add some sample data if the database is empty
        if not User.query.first():
            sample_user = User(username="test_user")
            db.session.add(sample_user)
            db.session.commit()
            
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

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True) 