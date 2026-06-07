import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

# .env file load karo
load_dotenv()

# Global client variable (reuse connection)
_client = None

def get_client():
    """MongoDB client banao (ek baar hi banata hai - singleton pattern)"""
    global _client

    if _client is None:
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        try:
            _client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
            # Connection test karo
            _client.admin.command("ping")
            print("✅ MongoDB se connection ho gaya!")
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"❌ MongoDB connection fail hua: {e}")
            _client = None
            raise

    return _client


def get_db():
    """Database object return karta hai"""
    db_name = os.getenv("DB_NAME", "trip_db")
    client = get_client()
    return client[db_name]


def get_collection(collection_name: str):
    """
    Kisi bhi collection ka object return karta hai.
    
    Usage:
        users = get_collection("users")
        users.find_one({"name": "Rahul"})
    """
    db = get_db()
    return db[collection_name]


def close_connection():
    """Connection band karo (app band hone pe call karo)"""
    global _client
    if _client is not None:
        _client.close()
        _client = None
        print("🔌 MongoDB connection band ho gaya.")