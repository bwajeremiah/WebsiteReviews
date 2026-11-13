from pymongo import MongoClient
import json

uri = "mongodb+srv://bwajeremiah_db_user:39firehouse@cluster0.hklay79.mongodb.net/"
client = MongoClient(uri)
import time


class Website:
    def __init__(self, url: str):
        self.url: str = url
        self.rating: int = 0
        self.easyNav: bool = False
        self.addFlood: bool = False
        self.notRealyFree: bool = False

    def to_dict(self):
        return {
        "url": self.url,
        "rating": self.rating,
        "easyNav": self.easyNav,
        "addFlood": self.addFlood,
        "notRealyFree": self.notRealyFree
    }