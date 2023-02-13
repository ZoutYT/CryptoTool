import motor.motor_asyncio
from model import Todo, crazy, price

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Austin:Austin2006825@todolist.pb8yqgh.mongodb.net/test')
database = client.Prices
collection = database.Converisons

async def fetch_one_conversion(Address):
    document = await collection.find_one({"Address": Address})
    return document

async def fetch_all_conversions():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(price(**document))
    return todos    

async def create_conversion(price):
    document = price
    result = await collection.insert_one(document)
    return document


async def update_conversion(title, addy):
    await collection.update_one({"title": title}, {"$set": {"Address": addy}})
    document = await collection.find_one({"title": title})
    return document

async def remove_conversion(Coin):
    await collection.delete_one({"Coin": Coin})
    return True

# async def fetch_all_names():
#     Names = []
#     cursor = collection2.find({})
#     async for document in cursor:
#         Names.append(crazy(**document))
#     return Names  

# async def create_crazy(name):
#     document = name
#     result = await collection2.insert_one(document)
#     return document