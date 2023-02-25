from bson.objectid import ObjectId
from app.database import UserCollection
from app.src.serializers.user import user_entity


# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in UserCollection.find():
        users.append(user_entity(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await UserCollection.insert_one(user_data)
    new_user = await UserCollection.find_one({"_id": user.inserted_id})
    return user_entity(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(user_id: str) -> dict:
    user = await UserCollection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_entity(user)


# Update a user with a matching ID
async def update_user(user_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await UserCollection.find_one({"_id": ObjectId(user_id)})
    if user:
        updated_user = await UserCollection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(user_id: str):
    user = await UserCollection.find_one({"_id": ObjectId(user_id)})
    if user:
        await UserCollection.delete_one({"_id": ObjectId(user_id)})
        return True
