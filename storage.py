from abc import ABC, abstractmethod
from config import USER, PASSWORD
import pymongo
from uuid import uuid4
from pathlib import Path
import json


class BaseStorage:
    @abstractmethod
    def create_car(self, car: dict):
        pass

    @abstractmethod
    def create_car_by_make(self):
        pass

    @abstractmethod
    def update_car(self):
        pass

    @abstractmethod
    def delete_car(self):
        pass


class MongoStorage(BaseStorage):
    def __init__(self):
        url = 'mongodb+srv://{user}:{password}@cluster0.tbcrbjt.mongodb.net/?retryWrites=true&w=majority'.format(
            user=USER, password=PASSWORD)

        client = pymongo.MongoClient(url)
        db = client['citations']

        self.collection = db['Cars']

    def create_car(self, car: dict) -> dict:
        car['uuid'] = str(uuid4())
        self.collection.insert_one(car)
        return car

    def create_car_by_make(self):
        raise NotImplemented

    def update_car(self):
        raise NotImplemented

    def delete_car(self):
        raise NotImplemented


storage = MongoStorage()
