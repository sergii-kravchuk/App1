from pymongo import MongoClient
from datetime import datetime


CONNECTION_STRING = "mongodb://root:root@mongodb1:27017"

database_name = "user-account"
collection_name = "users"

now = datetime.now()

document = {"user_id": 10, "user": "Sergii Kravchuk", "cur_time":now.strftime("%Y-%m-%d %H:%M:%S")}

client = MongoClient(CONNECTION_STRING)

dbloc = client[database_name]
colloc = dbloc[collection_name]

colloc.insert_one(document)

all_documents_cursor = colloc.find({})
print("All documents:")
for doc in all_documents_cursor:
    print(doc)