
from backend import notesFormat
from pymongo import MongoClient
import json
import time
from .websiteFormat import Website
from flask import Flask, jsonify,request
app = Flask(__name__)
uri = "mongodb+srv://bwajeremiah_db_user:39firehouse@cluster0.hklay79.mongodb.net/"
client = MongoClient(uri)

try:
    database = client.get_database("WebsiteReviews")
    websites = database.get_collection("Website")
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
@app.get("/api/website/")
def list_notes():
    all_websites = websites.find()
    return jsonify([Website(website["url"], website["rating"], website["easyNav"], website["adFlood"], website["notReallyFree"]).to_dict() for website in all_websites])
@app.get("/api/website/count")
def get_website_count():
    count = websites.count_documents({})
    return jsonify({"count": count})
@app.post("/api/website")
def add_website():
    data = request.get_json()
    new_website = {
        "url": data.get("url"),
        "rating": data.get("rating"),
        "easyNav": data.get("easyNav"),
        "adFlood": data.get("adFlood"),
        "notReallyFree": data.get("notReallyFree"),
    }
    websites.insert_one(new_website)
    return jsonify(new_website)
def main() -> None:
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()   