from flask import Flask, render_template, request, session, redirect, current_app, make_response
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

# Route for login
@app.route("/login", methods=["GET", "POST"])
def Login():

    if session.get('id') != None: # Allows access without account
        return redirect("/") 

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
            
            # Error if incorrect information is submitted
            else:
                return render_template("login.html", error="Incorrect username or password") # Renders login page with error message

    response = make_response("Login successful")
    response.headers['Cache-Control'] = 'no-store'

    return render_template("login.html") # Renders login page

# Route for logout
@app.route("/logout")
def Logout():
     session.clear()
     return redirect("/")

# Route for register
@app.route("/register", methods=["GET", "POST"])
def Register():

    if session.get('id') != None: # Allows access without account
        return redirect("/") 

    # Registers user if they submit the form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Attempts to add the user to the database
        if registerUser(username, password):
            # Returns to login page if successful for them to login
            return redirect("/login")
    
    return render_template("register.html") # Renders the page

# Route for posting reviews
@app.route("/postreview", methods=["GET", "POST"])
def Post():

    if session.get('id') == None: # Allows access if logged in
        return redirect("/") 

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

        # Return to My Reviews to see their post
        return redirect("/myreviews")

    return render_template("postreview.html") # Renders the page

# Route for page of all reviews
@app.route("/allreviews", methods=["GET", "POST"])
def Reviews():

    # Retrieve searched reviews, else return all reviews
    if request.method == 'POST':
        query = request.form.get('query', '')
        reviewData = searchReviews(query)

    else:
        reviewData = getAllReviews()

    return render_template('allreviews.html', reviews=reviewData) # Renders the page and sets the review data to a useable variable

# Route for page of user's reviews
@app.route("/myreviews")
def myReviews():

    if session.get('id') == None: # Allows access if logged in
        return redirect("/")

    # Retrieves the reviews of the logged in user
    user = session['username']
    reviewData = getMyReviews(user)
    
    return render_template("myreviews.html", reviews=reviewData) # Renders the page and sets the review data to a useable variable

# Route for page of an individual review
@app.route("/<int:id>")
def singleReview(id):

    # Gets the data for the review with id matching the page route
    reviewData = getSingleReview(id)
    if reviewData is None:
        redirect("/")

    return render_template("singlereview.html", review=reviewData) # Renders the page and sets the review data to a useable variable

# Route for deleting a review
@app.route("/<int:id>/delete", methods=("POST",))
def delete(id):

    deleteReview(id) # Deletes the selected review (see db.py)

    return redirect("/myreviews") # Renders the page

# Route for editing a review
@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):

    # Gets the review based on id
    reviewData = getSingleReview(id)

    # Only allows editing if they own the review - includes error handling for non-existant id
    try:
        if session.get('username') not in reviewData: # Allows access if logged in
                return redirect("/") 
    except:
        return redirect("/")

    if request.method== "POST":

        # Attempts to update review after they fill out the form
        reviewTitle = request.form['title']
        reviewDate = request.form['date']
        reviewerName = session['username']
        reviewText = request.form['description']
        rating = request.form['rating']
        reviewImage = request.files['image']

        # Retrieves the BLOB of the uploaded image to be stored
        reviewImage = reviewImage.read()

        # Stores the user's data in the previous review
        editReview(reviewTitle, reviewerName, reviewDate, reviewText, rating, reviewImage, id)

        # Return to My Reviews to see their post
        return redirect("/myreviews")
    
    return render_template("edit.html", review=reviewData) # Renders the page and sets the review data to a useable variable

# Converts BLOB images into a base64 to be converted to a proper image
def convertBLOB(reviewImage):
    byteArray = bytearray(reviewImage)  # Converts BLOB to Bytearray
    encodedData = base64.b64encode(bytes(byteArray)).decode('utf-8')  # Encodes Bytearray to base64
    
    return encodedData # Sends the real image back to what called it

@app.route('/serviceworker.js', methods=['GET'])
def sw():
    return current_app.send_static_file('serviceworker.js')

app.jinja_env.globals.update(convertBLOB=convertBLOB)

app.run(debug=True, port=5000) # Runs the Flask server