from typing import List, Dict

from pymongo import MongoClient


class Database:
    DEFAULT_USER = "default"
    USER_TAG = "user_id"

    def __init__(self, url, database):
        self._url = url
        self._database = database

    @property
    def _client(self):
        return MongoClient(self._url)

    def get_items_by_user(self, user_id: str = DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            return [doc for doc in db.items.find({self.USER_TAG: user_id})]

    def delete_items_by_user(self, items: List[str], user_id: str = DEFAULT_USER):
        [self.delete_item_by_user(item, user_id) for item in items]

    def delete_item_by_user(self, item: str, user_id: str = DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            return db.items.delete_many({"item": item, self.USER_TAG: user_id})

    def empty_list_by_user(self, user_id: str = DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            return db.items.delete_many({self.USER_TAG: user_id})

    def insert_items_by_user(self, items: List[Dict], user_id: str = DEFAULT_USER):
        with self._client as client:
            db = client[self._database]
            [d.update({self.USER_TAG: user_id}) for d in items]
            db.items.insert_many(items)
