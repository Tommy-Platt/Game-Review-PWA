from flask import Flask, render_template, request
import db

app = Flask(__name__)
app.secret_key = "revos"

# Route for homepage
@app.route("/")
def Home():
    return render_template("index.html")

app.run(debug=True, port=5000) # Runs the Flask server