import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

@st.cache_resource
def get_client():
    try:
        uri = st.secrets["mongodb"]["uri"]
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        return client
    except KeyError:
        st.error("❌ MongoDB URI secrets mein nahi mili. Secrets configure karein.")
        return None
    except (ConnectionFailure, ConfigurationError) as e:
        st.error(f"❌ MongoDB connection failed: {e}")
        return None


def get_db():
    try:
        db_name = st.secrets["mongodb"]["database"]
        client = get_client()
        if client:
            return client[db_name]
        return None
    except KeyError:
        st.error("❌ Database name secrets mein nahi mila.")
        return None


def get_collection(collection_name: str):
    db = get_db()
    if db is not None:
        return db[collection_name]
    return None