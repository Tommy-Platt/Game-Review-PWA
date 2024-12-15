from flask import Flask, render_template, request
from db import *

app = Flask(__name__)
app.secret_key = "revos"

# Route for homepage
@app.route("/")
def Home():
    reviewData = getAllReviews()
    return render_template("index.html", reviews=reviewData) # Renders homepage and sets the review data to a useable variable

app.run(debug=True, port=5000) # Runs the Flask server