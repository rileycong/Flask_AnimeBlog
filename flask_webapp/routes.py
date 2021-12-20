from flask import render_template, url_for, flash, redirect
from flask_webapp import app
from flask_webapp.forms import RegistrationForm, LoginForm
from flask_webapp.models import User, Post

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

@app.route("/rate")
def rate():
    return render_template('rate.html', title = 'Rate')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('Okay bro you are in the hood', 'success')
            return redirect(url_for('home'))
        else:
            flash('LOL you failed even the simplist stuff. Check again mate!', 'danger')
    return render_template('login.html', title='Login', form=form)