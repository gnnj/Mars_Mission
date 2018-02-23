# Flask
from flask import Flask, render_template, redirect
app = Flask(__name__)

# Mongo DB
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_scrape

collection = db.mars_scrape

# Import scrape function
from scrape_mars import Scrape

@app.route("/")
def home():
    scrape_dict = db.collection.find_one()
    return render_template("index.html", dict=scrape_dict)

@app.route("/scrape")
def reload():
    mars_dict = scrape()
    db.collection.update({"id": 1}, {"$set": mars_dict}, upsert = True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == '__main__':
    app.run(debug=True)