import motor.motor_asyncio
from app.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
database = client[settings.DATABASE_NAME]
UserCollection = database.get_collection("users")