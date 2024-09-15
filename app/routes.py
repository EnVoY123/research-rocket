from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from app.models import User
from flask import Response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can log in now.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your credentials.', 'danger')
            return Response(status=403, response='Login failed. Check your credentials.')
    return render_template('login.html')