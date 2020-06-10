from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://127.0.0.1:27017/Mars_mission")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    mongo.db.mars.update({}, mars_data, upsert = True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
