from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.src.models.user import (
    ErrorResponseSchema,
    ResponseSchema,
    UserSchema,
    UsersListSchema,
    UpdateUserSchema,
)
from app.src.service.user import (
    add_user,
    retrieve_users,
    retrieve_user,
    update_user,
    delete_user,
)

router = APIRouter()


@router.get("/", response_model=UsersListSchema, response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseSchema(users, "Users data retrieved successfully")
    return ResponseSchema(users, "Empty list returned")


@router.post("/", response_description="A new user added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseSchema(new_user, "User added successfully.")


@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(user_id):
    user = await retrieve_user(user_id)
    if user:
        return ResponseSchema(user, "User data retrieved successfully")
    return ErrorResponseSchema("An error occurred.", 404, "user doesn't exist.")


@router.put("/{id}")
async def update_user_data(user_id: str, req: UpdateUserSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(user_id, jsonable_encoder(req))
    if updated_user:
        return ResponseSchema(
            f"User with ID: {user_id} update is successful.",
            "User updated successfully",
        )
    return ErrorResponseSchema(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(user_id: str):
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return ResponseSchema(
            f"User with ID: {user_id} removed.", "User deleted successfully"
        )
    return ErrorResponseSchema(
        f"An error occurred", 404, "user with id {user_id} doesn't exist."
    )