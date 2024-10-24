# Import necessary modules
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from youtube_transcriptor import get_and_save_transcript
from models import db, User
import os
import re
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define route for the main page, accepting both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # Add welcome message
    welcome_message = f'Welcome, {current_user.first_name}!'
    
    if request.method == 'POST':
        # If it's a POST request, we're receiving form data
        # Get the YouTube URL and language from the form
        video_url = request.form['video_url']
        language = request.form['language']
        
        # Generate a unique filename for this transcript
        # os.urandom(4).hex() creates a random 8-character string
        output_file = f"transcript_{os.urandom(4).hex()}.txt"
        
        try:
            # Call our function to get and save the transcript
            get_and_save_transcript(video_url, output_file, language)
            
            # Send the file to the user for download
            return send_file(output_file, as_attachment=True)
        except Exception as e:
            # If an error occurs, render the template with an error message
            return render_template('index.html', error=str(e))
        finally:
            # Clean up the file after sending or if an error occurred
            if os.path.exists(output_file):
                os.remove(output_file)
    
    # For GET requests, just render the form
    return render_template('index.html', welcome_message=welcome_message)

# Define route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        ip_address = request.remote_addr
        
        # Check if the email is already registered
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        
        # Check password requirements
        if not is_password_valid(password):
            flash('Password does not meet the requirements')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(email=email, username=User.generate_username(), 
                        ip_address=ip_address, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registered successfully')
        return redirect(url_for('login'))
    
    return render_template('register.html')

def is_password_valid(password):
    """
    Check if the password meets the requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Define route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
    
    return render_template('login.html')

# Define route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
