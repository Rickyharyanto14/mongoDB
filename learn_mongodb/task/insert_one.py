import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Insert Document (Single)
collection = mydb['my_book']
data = [
    {
     "nama" : "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 235000,
     "stock" : 4
    }
]

for record in data:
    collection.insert_one(record)
    
# Write the data to a CSV file
with open('learn_mongodb/output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])