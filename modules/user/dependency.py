from fastapi import Depends
from pymongo import MongoClient
from core.database import user_collection

def get_db():
    db = user_collection
    try:
        yield db
    finally:
        db.client.close()

        