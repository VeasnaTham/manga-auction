from fastapi import Depends
from pymongo import MongoClient
from core.database import manga_collection

def get_db():
    db = manga_collection
    try:
        yield db
    finally:
        db.client.close()

