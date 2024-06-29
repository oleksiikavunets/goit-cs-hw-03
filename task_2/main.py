import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

BASE_DIR = Path(__file__).parent.parent
MOVIES_FILENAME_CSV = BASE_DIR / 'data' / 'movies.csv'

load_dotenv(BASE_DIR / '.env')

DB_HOST = os.getenv('MONGO_DB_HOST')
DB_NAME = os.getenv('MONGO_INITDB_DATABASE')
DB_USER = os.getenv('MONGO_INITDB_ROOT_USERNAME')
DB_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
DB_PORT = os.getenv('MONGO_DB_PORT')

URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"


class CatsDb:
    def __init__(self, uri):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client.book

    def insert_cat(self, name, age, features):
        data = {'name': name, 'age': age, 'features': features}
        result = self.db.cats.insert_one(data)
        print(result)

    def show_all(self):
        cats = self.db.cats.find({})
        [print(cat) for cat in cats]

    def show_cat(self):
        name = input('Enter cat`s name: ')
        cat = self.db.cats.find_one({'name': name})
        if cat:
            print(cat)
        else:
            print(f'Could not find cat with name "{name}".')

    def set_age(self, name, age):
        result = self.db.cats.update_one({"name": name}, {"$set": {"age": age}})
        if result.matched_count:
            print(result)
        else:
            print(f'Could not find cat with name "{name}".')

    def add_feature(self, name, feature):
        result = self.db.cats.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count:
            print(result)
        else:
            print(f'Could not find cat with name "{name}".')

    def delete_cat(self, name):
        result = self.db.cats.delete_one({'name': name})
        if result.deleted_count:
            print(result)
        else:
            print(f'Could not find cat with name "{name}".')

    def delete_all(self):
        print(self.db.cats.delete_many({}))


if __name__ == '__main__':
    cats_db = CatsDb(URI)

    cats_db.insert_cat('Tom', 5, ['red', 'heavy'])
    cats_db.insert_cat('Simba', 12, ['black', 'kind'])
    cats_db.insert_cat('Jerry', 6, ['white', 'furious'])

    cats_db.show_all()

    cats_db.show_cat()

    cats_db.set_age('Tom', 19)

    cats_db.show_all()

    cats_db.set_age('Juan', 19)

    cats_db.add_feature('Jerry', 'hungry')

    cats_db.show_all()

    cats_db.add_feature('Juan', 'nasty')

    cats_db.delete_cat('Simba')

    cats_db.show_all()

    cats_db.delete_cat('Juan')

    cats_db.delete_all()

    cats_db.show_all()

    print()

