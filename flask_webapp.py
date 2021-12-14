from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Home page</h1>"

@app.route("/about")
def about():
    return "<h1>About the noob behind this</h1>"

@app.route("/rate")
def rate():
    return "<h1>Rate Anime</h1>"

if __name__ == '__main__':
    app.run(debug=True)