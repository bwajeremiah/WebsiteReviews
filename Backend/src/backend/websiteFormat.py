from pymongo import MongoClient
import json

uri = "mongodb+srv://bwajeremiah_db_user:39firehouse@cluster0.hklay79.mongodb.net/"
client = MongoClient(uri)
import time


class Website:
    def __init__(self, url: str, rating: int = 0, easyNav: bool = False, adFlood: bool = False, actuallyFree: bool = False):
        self.url: str = url
        self.rating: int = rating
        self.easyNav: bool = easyNav
        self.adFlood: bool = adFlood
        self.actuallyFree: bool = actuallyFree

    def to_dict(self):
        return {
        "url": self.url,
        "rating": self.rating,
        "easyNav": self.easyNav,
        "adFlood": self.adFlood,
        "actuallyFree": self.actuallyFree
    }