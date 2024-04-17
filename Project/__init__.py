from flask import Flask
from flask import render_template, redirect, url_for, request
from Project.DBManager import authenticate_user, create_user;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    print(authenticate_user(email, password))
    
    return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    create_user(email, name, password, 'C')

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return 'Logout'
