from abc import ABC, abstractmethod
from config import USER, PASSWORD
import pymongo
from uuid import uuid4


class BaseStorage:
    @abstractmethod
    def create_car(self, car: dict):
        pass

    @abstractmethod
    def get_cars(self, skip: int = 0, limit: int = 10, search_param: str = None):
        pass

    @abstractmethod
    def update_car(self, car_uuid: str, new_price: float):
        pass

    @abstractmethod
    def delete_car(self, book_uuid: str):
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

    def get_cars(self, skip: int = 0, limit: int = 10, search_param: str = None):
        query = {}
        if search_param:
            print(search_param)
            query = {'mark': {'$regex': search_param.strip()}}
        return self.collection.find(query).skip(skip).limit(limit)

    def update_car(self, car_uuid: str, new_price: float):
        filter_data = {'uuid': car_uuid}
        new_data = {'$set': {'price': new_price}}
        processed = self.collection.update_one(filter_data, new_data)
        return processed

    def delete_car(self, book_uuid: str):
        filter_data = {'uuid': book_uuid}
        self.collection.delete_one(filter_data)


storage = MongoStorage()
