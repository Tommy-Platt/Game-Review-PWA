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
