from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

class UserInDB(User):
    id: int
