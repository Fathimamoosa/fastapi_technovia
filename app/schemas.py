from pydantic import BaseModel, EmailStr


class UserFormSchema(BaseModel):
    name: str
    email: EmailStr
    message: str


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    message: str

    class Config:
        from_attributes = True