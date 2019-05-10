from typing import List, Dict

from pymongo import MongoClient


class Database:

    DEFAULT_USER = "default"
    USER_TAG = "user_id"

    def __init__(self, host, port, database):
        self._host = host
        self._port = port
        self._database = database

    @property
    def _client(self):
        return MongoClient(self._host, self._port)

    def get_items_by_user(self, user_id: str=DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            return [doc for doc in db.items.find({self.USER_TAG: user_id})]

    def delete_items_by_user(self, user_id: str=DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            return db.items.delete_many({self.USER_TAG: user_id})

    def insert_items_by_user(self, items: List[Dict], user_id: str=DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            [d.update({self.USER_TAG: user_id}) for d in items]
            db.items.insert_many(items)
