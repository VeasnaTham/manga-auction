from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from modules.manga.model import Item
from pymongo import MongoClient
from modules.manga.dependency import get_db
from core.database import manga_collection

router = APIRouter(
    prefix="/manga",
    tags=["Manga"]
)

#Create
@router.post("/mangas/", response_model=Item)
async def create_item(item: Item, db: MongoClient = Depends(get_db)):
    item_dict = item.dict()
    result = db.insert_one(item_dict)
    book_id = result.inserted_id
    return {**item_dict, "id": str(book_id)}

#Read
@router.get("/mangas/{book_id}")
async def read_item(book_id: str,):
    try:
        result = manga_collection.find_one({"_id": ObjectId(book_id)})
        if result:
            print(result)
            result['id'] = str(result.pop('_id'))
            return result
        raise HTTPException(status_code=404, detail=f"Item with ID {book_id} not found")
    except Exception as e:
        print("Error", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

#Update
@router.put("/mangas/{book_id}", response_model=Item)
async def update_item(book_id: str, item: Item, db: MongoClient = Depends(get_db)):
    result = db.update_one({"_id": ObjectId(book_id)}, {"$set": item.dict()})
    if result.modified_count == 1:
        return {**item.dict(), "id": book_id}
    raise HTTPException(status_code=404, detail=f"Item with ID {book_id} not found")

#Delete
@router.delete("/mangas/{book_id}", response_model=dict)
async def delete_item(book_id: str, db: MongoClient = Depends(get_db)):
    result = db.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Item with ID {book_id} not found")

#Get all
@router.get('/')
async def get(db: MongoClient = Depends(get_db)):
    data = list(db.find())
    for item in data:
        if isinstance(item.get('_id'), ObjectId):
            item['id'] = str(item.pop('_id'))
    return {'data': data}

#Update by ID
@router.put('/mangas/update_manga/{book_id}')
async def update_by_ID(book_id: str, bid: float):
    manga = manga_collection.find_one({"_id": ObjectId(book_id)})

    price = manga.get("price", 0)
    currentBid = manga.get('bid', 0)
    

    if bid <= price:
        raise HTTPException(status_code=400, detail="Please bid higher than the current price")

    if bid > price * 1.5:
        raise HTTPException(status_code=400, detail=f"Maximum bid for this manga is {price * 1.5}")

    updated_data = {"$set": {"bid": bid}}
    result = manga_collection.update_one({"_id": ObjectId(book_id)}, updated_data)

    if result.modified_count == 1:
        raise HTTPException(status_code=200, detail="Bid successfully")
    else:
        raise HTTPException(status_code=500, detail="Failed to Bid")