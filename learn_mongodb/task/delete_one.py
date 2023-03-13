import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Insert Document
collection = mydb['my_book']

# Delete one document
query = {'nama': 'Harry Potter and the Chamber of Secrets (Harry Potter, #2)'}
result = collection.delete_one(query)

# Print the deleted data
pprint(f'{result.deleted_count} document(s) deleted')