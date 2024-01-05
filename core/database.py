from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://thamveasna123:BZVFme3n2W2mmhDx@onlinebidding.j6ohcyl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client.mangaDB
manga_collection = db.manga 
user_collection = db.user