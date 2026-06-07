# database/connection.py
import os
import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_database():
    """Get MongoDB database connection using Streamlit secrets or env variable."""
    try:
        # Try Streamlit secrets first (for deployment)
        mongo_uri = st.secrets.get("MONGO_URI", None)
    except Exception:
        mongo_uri = None

    if not mongo_uri:
        # Fallback to environment variable
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")  # Validate connection
        db = client["manali_trip"]
        return db
    except ConnectionFailure as e:
        st.error(f"❌ MongoDB Connection Failed: {e}")
        return None
    except Exception as e:
        st.error(f"❌ Database Error: {e}")
        return None


def get_collection(collection_name: str):
    """Get a specific collection from the database."""
    db = get_database()
    if db is not None:
        return db[collection_name]
    return None