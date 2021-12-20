from flask import render_template, url_for, flash, redirect, request
from flask_webapp import app, db, bcrypt
from flask_webapp.forms import RegistrationForm, LoginForm
from flask_webapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Wibu 1',
        'title': 'GTO and the state of adulthood',
        'content': 'Basically a great show!',
        'date_posted': 'April 20, 2017'
    },
    {
        'author': 'Protagonist wannabe',
        'title': 'Spoilers for Made in Abyss',
        'content': 'Another day another spoiler',
        'date_posted':'April 21, 2017' 
    },
    {
        'author': 'hMmn',
        'title': 'Dead dead demon and the Isino humor',
        'content': 'Too busy monitoring the internet',
        'date_posted':'July 21, 2020' 
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Welcome to the gang ;)', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('LOL you failed even the simplist stuff. Check again mate!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')