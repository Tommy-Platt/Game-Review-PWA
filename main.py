from flask import Flask, render_template, request, session, redirect
from db import *

app = Flask(__name__)
app.secret_key = "revos"

# Route for homepage
@app.route("/")
def Home():
    reviewData = getAllReviews()
    return render_template("index.html", reviews=reviewData) # Renders homepage and sets the review data to a useable variable

@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            # Checks if details are correct
            user = checkLogin(username, password)
            if user:
                # Save username and id to the current session
                session['id'] = user['id']
                session['username'] = user['username']

                # Return to homepage
                return redirect("/")

    return render_template("login.html")

app.run(debug=True, port=5000) # Runs the Flask server