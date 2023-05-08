import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
"""create conection to MONGO DB"""
client = pymongo.MongoClient(
    f'mongodb+srv://{os.getenv("NAME")}:{os.getenv("PASSWORD")}@testmongodb.rfvtxbv.mongodb.net/')

"""conection to local mongo"""
# local_client = pymongo.MongoClient('mongodb://allexx:allexx@localhost:27017/?authMechanism=DEFAULT')


local_client = pymongo.MongoClient('mongodb://localhost:27017')

"""change DB"""
# db = client.test

db = local_client.test


"""change collection"""
coll = db.new_tab

"""add data to collection"""
coll.insert_one({'_id': 1, 'name': '444', 'male': 'F'})
