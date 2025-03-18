from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME

class MongoConnector:
    def __init__(self, uri=MONGO_URI, db_name='video_indexing'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_scene_data(self, collection, data):
        collection = self.db[collection]
        return collection.insert_one(data)

    def fetch_scene_data(self, collection, query):
        collection = self.db[collection]
        return collection.find(query)
