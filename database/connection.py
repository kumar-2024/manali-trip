import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

_client = None

def get_client():
    global _client

    if _client is None:
        mongo_uri = st.secrets["MONGO_URI"]   # 🔥 FIX HERE

        try:
            _client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
            _client.admin.command("ping")
            print("✅ MongoDB connected successfully")

        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"❌ MongoDB connection failed: {e}")
            _client = None
            raise

    return _client