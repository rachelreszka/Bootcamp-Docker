from beanie import init_beanie
import motor.motor_asyncio
from server.models.noticias import Noticias
import pymongo


async def init_db():
    uri = "mongodb://dba:qwe123@172.18.0.2:27017/"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client.db_noticias, document_models=[Noticias])

#async def do_find():
    #cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
    #for document in await cursor.to_list(length=100):
        #pprint.pprint(document)


#client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://dba:qwe123@172.18.0.2/db_noticias?retryWrites=true&w=majority")
 #await init_beanie(database=client.db_name, document_models=[Noticias])
 
 


     #"mongodb://dba:qwe123@172.18.0.2/db_noticias:27017/"
    #f"mongodb://user:pass@host:27017/beanie_db"
 #"mongodb://localhost:27017/productreviews"