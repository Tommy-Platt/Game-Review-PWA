from flask import Flask, render_template, request, session, redirect
from db import *
from PIL import Image
import base64, io

app = Flask(__name__)
app.secret_key = "revos"

# Route for homepage
@app.route("/")
def Home():
    reviewData = getRecentReviews()
    
    return render_template("index.html", reviews=reviewData) # Renders homepage and sets the review data to a useable variable

@app.route("/login", methods=["GET", "POST"])
def Login():

    # Attempts login after form is submitted
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

@app.route("/logout")
def Logout():
     session.clear()
     return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def Register():

    # Registers user if they submit the form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Attempts to add the user to the database
        if registerUser(username, password):
            # Returns to login page if successful for them to login
            return redirect("/login")
    
    return render_template("register.html")

@app.route("/postreview", methods=["GET", "POST"])
def Post():

    # Attempts to add review after they fill out the form
    if request.method == "POST":
        reviewTitle = request.form['title']
        reviewDate = request.form['date']
        reviewerName = session['username']
        reviewText = request.form['description']
        rating = request.form['rating']
        reviewImage = request.files['image']

        # Retrieves the BLOB of the uploaded image to be stored
        reviewImage = reviewImage.read()

        # Stores the user's data
        postReview(reviewTitle, reviewDate, reviewerName, reviewText, rating, reviewImage)

    return render_template("postreview.html")

@app.route("/allreviews")
def Reviews():
    reviewData = getAllReviews()
    
    return render_template("allreviews.html", reviews=reviewData) # Renders the page and sets the review data to a useable variable

@app.route("/myreviews")
def myReviews():
    user = session['username']
    reviewData = getMyReviews(user)
    
    return render_template("myreviews.html", reviews=reviewData) # Renders the page and sets the review data to a useable variable

# Converts BLOB images into a base64 to be converted to a proper image
def convertBLOB(reviewImage):
    byteArray = bytearray(reviewImage)  # Convert BLOB to Bytearray
    encodedData = base64.b64encode(bytes(byteArray)).decode('utf-8')  # Encode bytearray to base64
    
    return encodedData # Sends the real image back to what called it

app.jinja_env.globals.update(convertBLOB=convertBLOB)

app.run(debug=True, port=5000) # Runs the Flask server