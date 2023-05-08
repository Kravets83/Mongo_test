'''From docs mongoDB'''

import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

uri = f"mongodb+srv://{os.getenv('NAME')}:{os.getenv('PASSWORD')}@testmongodb.rfvtxbv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

'''connect or create DB second_test'''
db = client.second_test

'''create collections users'''
coll = db.users

'''add document to collections users'''
# try:
#     coll.insert_one({'_id': 2, 'name': '444', 'male': 'F'})
#     print('user add to DB')
# except Exception as e:
#     print(e)

'''add many docs'''
# data_many = [
#     {
#         '_id': 3,
#         'name': 'wwww',
#         'male': 'M'
#     },
#     {
#         '_id': 4,
#         'name': 'wwww4',
#         'male': 'M'
#     },
# ]
# try:
#     coll.insert_many(data_many)
#     print('users add to DB')
# except Exception as e:
#     print(e)


'''get all docs,
second dictionary what show
.limit(N) N first docs'''
docs = [doc for doc in coll.find({}, {'_id': 1, 'name': 0}).limit(3)]
print(docs)

'''get selections'''

data = {'male': 'M', 'name': 'wwww'}

docs = [doc for doc in coll.find(data)]
# docs = [doc for doc in coll.find({'_id':0, 'name': 1}]

print(docs)
