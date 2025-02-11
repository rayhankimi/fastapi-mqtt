from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import os

# URL MongoDB
MONGODB_URL = os.environ.get("MONGODB_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "")


class MongoConnection:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        """MongoDB Connection Initialization"""
        try:
            self.client = AsyncIOMotorClient(MONGODB_URL)
            self.db = self.client[DATABASE_NAME]
            print("Connected to MongoDB")
        except PyMongoError as e:
            print(f"Error: {e}")
            print(MONGODB_URL + DATABASE_NAME)

    async def disconnect(self):
        """MongoDB Connection Termination"""
        self.client.close()
        print("Disconnected from MongoDB")


mongo_connection = MongoConnection()
