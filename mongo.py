import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "Dehydra"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_docs = [{'dish': 'Wortel', 'hydra_temp': '57', 'hydra_time': ' 6 to 10 hours', 'blanch': True},
# {'dish': 'Bieslook', 'hydra_temp': '35', 'hydra_time': ' 5 to 6 hours', 'blanch': False},
# {'dish': 'Thijm', 'hydra_temp': '35', 'hydra_time': '10 to 14 hours', 'blanch': False},
# {'dish': 'Rozemarijn', 'hydra_temp': '35', 'hydra_time': '9 to 12 hours', 'blanch': False},
# {'dish': 'Bleekselderij blad', 'hydra_temp': '35', 'hydra_time': ' 2 to 4 hours', 'blanch': False}]

# coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)