import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def getDB():

    # Connect to reviewos.db and return the object db
    db = sqlite3.connect(".database/reviewos.db")
    db.row_factory = sqlite3.Row

    return db

def getAllReviews():

    # Connect to reviewos.db, SELECT all reviews and return
    db = getDB()
    reviews = db.execute("SELECT * FROM Reviews ORDER BY reviewDate DESC").fetchall()
    db.close()
    return reviews

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
    db.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, hash,))
    db.commit()

    return True