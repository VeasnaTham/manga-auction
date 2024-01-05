from pydantic import BaseModel

class Item(BaseModel):
    title: str
    category: str
    genre: list
    price: float
    img: str
    description: str
    time: int
    bid: float

