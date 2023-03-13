import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB Databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

collection = mydb['my_book']

# Insert records using List
myBookList = [
    {
     "nama" : "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 185000,
     "stock" : 3
    },
    {
     "nama" : "Harry Potter and the Order of the Phoenix (Harry Potter, #5)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 170000,
     "stock" : 1
    },
    {
     "nama" : "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 220000,
     "stock" : 9
    },
    {
     "nama" : "Harry Potter and the Chamber of Secrets (Harry Potter, #2)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 245000,
     "stock" : 4
    },
    {
     "nama" : "Harry Potter Collection (Harry Potter, #1-6)",
     "author" : "J.K. Rowling",
     "tags" : "Novel",
     "harga" : 1545000,
     "stock" : 6
    }
]

# Insert many (List) to collection
collection.insert_many(myBookList)
    
# Write the data to a CSV file
with open('learn_mongodb/output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])