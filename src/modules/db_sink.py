# Connect to mongodb instance
# It should have a function to save events to the mongodb collection

# Gundeep
#Importing the Things first
import sys, os
from pymongo import MongoClient
import datetime

# Add root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from config.config import config

# Create MongoDB client
client = MongoClient(config.MONGO_URI)

# Select DB and Collection
db = client["log_aggregator"]
log_collection = db["logs"]

def store_log(log_data):
    """
    Inserts a log entry into the MongoDB collection.
    `log_data` should be a dictionary.
    """
    log_data["received_at"] = datetime.datetime.utcnow()
    
    try:
        result = log_collection.insert_one(log_data)
        print(f"[✓] Log inserted with ID: {result.inserted_id}")
    except Exception as e:
        print(f"[✗] Error inserting log: {e}")

