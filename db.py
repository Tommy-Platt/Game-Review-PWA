import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def getDB():

    # Connect to reviewos.db and return the object db
    db = sqlite3.connect(".database/reviewos.db")
    db.row_factory = sqlite3.Row

    return db

def getAllReviews():

    # Connect to reviewos.db, SELECT all reviews and return, joining the reviewer name with their username
    db = getDB()
    reviews = db.execute("""SELECT * FROM Reviews JOIN Users ON Reviews.reviewerName = Users.username ORDER BY reviewDate DESC""").fetchall()
    db.close()
    return reviews

def getRecentReviews():

    # Connect to reviewos.db, SELECT the 5 most recent reviews and return
    db = getDB()
    reviews = db.execute("SELECT * FROM Reviews ORDER BY reviewDate DESC LIMIT 5").fetchall()
    db.close()
    return reviews

def getMyReviews(user):

    # Passed session username used to return all reviews in the Reviews table by that user
    db = getDB()
    reviews = db.execute(f"SELECT * FROM Reviews WHERE reviewerName='{user}' ORDER BY reviewDate DESC").fetchall()
    db.close()
    return reviews

def getSingleReview(id):
    
    # Retrieves the important information for one review
    db = getDB()
    review = db.execute(f"SELECT * FROM Reviews WHERE id={id}").fetchone()
    db.close()

    return review

def checkLogin(username, password):

    db = getDB()

    # Retrieve single user from the DB matching the username
    user = db.execute("SELECT * FROM Users WHERE username=? COLLATE NOCASE", (username,)).fetchone()

    # Checks if the user exists in the database
    if user is not None:
        # Checks if the password is correct
        if check_password_hash(user['password'], password):
            return user
        
    # Returns None if incorrect info is input
    return None

def registerUser(username, password):

    # Checks if user enters username and password
    if username is None or password is None:
        return False
    
    # Adds the entered information to Users table in database
    db = getDB()
    hash = generate_password_hash(password)
    # Try to insert the user into the database, if it fails the page refreshes
    try:
        db.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, hash,))
        db.commit()
    except:
        return False

    return True

def postReview(title, reviewerName, reviewDate, reviewText, rating, reviewImage):

    # If any required field is missing info, refresh page
    for i in (title, reviewerName, reviewDate, reviewText, rating):
        if i is None:
            return False

    # Ratings acceped are only 1-5, returns false with other numbers and if another datatype is used
    try:
        if int(rating) not in range(1,6):
            return False
    except:
        return False

    # Adds the entered information to Reviews table in database
    db = getDB()
    db.execute("INSERT INTO Reviews(title, reviewDate, reviewerName, reviewText, rating, reviewImage) VALUES(?, ?, ?, ?, ?, ?)", (title, reviewerName, reviewDate, reviewText, rating, reviewImage))
    db.commit()
    
    return True