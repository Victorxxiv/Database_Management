from pymongo import MongoClient, errors
import os
from pymongo.server_api import ServerApi

# Replace with your connection string
connection_string = os.getenv('MONGODB_CONNECTION_STRING')
try:
    # Create a MongoClient instance with a ServerApi version
    client = MongoClient(connection_string, server_api=ServerApi('1'))

    # Test the connection by listing databases
    print("Testing connection...")
    print("Databases:")
    for db_name in client.list_database_names():
        print(f"- {db_name}")

    # Access a database
    db = client.test_database  # Replace 'test_database' with your database name

    # List all collections in the database
    print(f"\nCollections in the database '{db.name}':")
    for collection_name in db.list_collection_names():
        print(f"- {collection_name}")

    # Access a collection
    collection = db.test_collection  # Replace 'test_collection' with your collection name

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
