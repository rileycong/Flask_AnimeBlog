from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)