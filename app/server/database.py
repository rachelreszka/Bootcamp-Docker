from beanie import init_beanie
import motor.motor_asyncio
from server.models.noticias import Noticias
import pymongo


async def init_db():
    #uri = "mongodb://dba:qwe123@172.18.0.3:27017/"
    uri = "mongodb://codracc:kljKDT3109IV73nTbX0kWeqnvMQfAA8CHD98sZ9itXnwUIiQTwB7xoKSm8oXZFSKmWKANWo14bFHk4eSkWT64w==@codracc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@codracc@/"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client.db_noticias, document_models=[Noticias])