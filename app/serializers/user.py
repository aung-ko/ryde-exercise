def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "dob": user["dob"],
        "address": user["address"],
        "description": user["description"],
        "created_at": user["created_at"],
    }
