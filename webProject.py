from flask import *
import urllib.request

app = Flask(__name__) #magic line

@app.route("/") #tell flask which URL should run this method and which methods to accept/look for
def home():
    return render_template("home.html")

@app.route("/scratch", methods = ["GET", "POST"]) #tell flask which URL should run this method and which methods to accept/look for
def scratch():
    return render_template("scratch.html")

@app.route("/about") #tell flask which URL should run this method and which methods to accept/look for
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)