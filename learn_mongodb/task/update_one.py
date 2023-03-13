import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Insert Document
collection = mydb['my_book']

# Update (One) stock field
query = {"nama": "Harry Potter and the Goblet of Fire (Harry Potter, #4)"}
updated_stock = {"$set":{"harga": 270000,"stock": 11}}

collection.update_one(query,updated_stock)

# Write the data to a CSV file
with open('learn_mongodb/output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])