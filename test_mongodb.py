import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get DB URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to MongoDB
client = MongoClient(DATABASE_URL)

# Get database (will be "Network-Security")
db = client.get_database()

# Create a collection "users"
users = db["users"]

# Insert a sample document (this creates the DB & collection)
users.insert_one({"username": "admin", "role": "superuser"})

print("Database and collection created successfully!")
print(users.find_one({"username": "admin"}))
