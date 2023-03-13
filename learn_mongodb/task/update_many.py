import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Insert Document
collection = mydb['my_book']

# Update (Many) Stock and Price fields
new_updates = [
    {
        'query' : {"nama": "Harry Potter and the Goblet of Fire (Harry Potter, #4)"},
        'update' : {"$set":{"harga": 265000,"stock": 14}}
    },
    { 
        'query' : {"nama": "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"},
        'update' : {"$set":{"harga": 185000,"stock": 5}}
    },
    { 
        'query' : {"nama": "Harry Potter and the Order of the Phoenix (Harry Potter, #5)"},
        'update' : {"$set":{"harga": 195000}}
    },
    ]
# Update the documents
for update in new_updates:
    collection.update_many(update['query'], update['update'], upsert=True)

# Write the data to a CSV file
with open('learn_mongodb/output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])