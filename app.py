from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://127.0.0.1:27017")

@app.route("/"):
    def home:
        

if __name__ == "__main__":
    app.run(debug=True)