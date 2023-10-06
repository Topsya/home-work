  
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
 

uri = "mongodb+srv://topsya1986:topsya1986@cluster0.jyxrtyu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.homework9





 