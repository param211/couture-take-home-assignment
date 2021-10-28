from pydantic import BaseModel, Field, EmailStr


# basic schema to store user data
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Firstname Lastname",
                "email": "test@example.com",
                "password": "abcdxyz",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {"example": {"email": "test@example.com", "password": "abcdxyz"}}
