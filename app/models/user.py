from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Any, List, Optional


class UserSchema(BaseModel):
    username: str = Field(...)
    dob: date = Field(...)
    address: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(datetime.now())


class UserOneSchema(UserSchema):
    id: str

class UsersListSchema(BaseModel):
    data: List[UserOneSchema]
    code: int
    message: str


class UpdateUserSchema(BaseModel):
    username: Optional[str]
    dob: Optional[date]
    address: Optional[str]
    description: Optional[str]


def ResponseSchema(data: Any, message: str) -> dict:
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseSchema(error: str, code: str, message: str) -> dict:
    return {"error": error, "code": code, "message": message}
