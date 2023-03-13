import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Insert Document
collection = mydb['my_book']

# Query the database for records with stock less than (lt) 5 and harga greater than (gt) 100000
query = {"stock": {"$lt": 5}, "harga": {"$gt": 100000}}
results = collection.find(query)

# Read the data to a CSV file
with open('learn_mongodb/output/data.csv', mode='r', newline='') as file:
    writer = csv.reader(file)
    for record in results:
        # Print data
        pprint(record)