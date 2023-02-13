from pydantic import BaseModel

class Todo(BaseModel):
    Chain : str
    Coin : str
    Address: str

class crazy(BaseModel):
    title: str

class price(BaseModel):
    Coin :str
    Price: str
    Amount : str