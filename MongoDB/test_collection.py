from pymongo import MongoClient, errors
import os
from pymongo.server_api import ServerApi

# Replace with your connection string
connection_string = os.getenv('MONGODB_CONNECTION_STRING')

try:
    # Create a MongoClient instance with a ServerApi version
    client = MongoClient(connection_string, server_api=ServerApi('1'))

    # Access a database
    db = client.test_database  # Replace 'test_database' with your database name

    # Access a collection
    collection = db.test_collection  # Replace 'test_collection' with your collection name

    # Insert a sample document if collection is empty
    if collection.count_documents({}) == 0:
        collection.insert_one({"name": "example", "value": 123})
        print("Inserted a sample document into 'test_collection'.")

    # Print all documents in the collection
    print(f"\nDocuments in the collection '{collection.name}':")
    for doc in collection.find():
        print(doc)

except errors.ConnectionError as ce:
    print(f"Connection error: {ce}")
except errors.PyMongoError as pme:
    print(f"PyMongo error: {pme}")
finally:
    # Close the connection
    client.close()
    print("\nConnection closed.")
