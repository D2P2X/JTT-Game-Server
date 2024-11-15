from pydantic import BaseModel

class ResponseData(BaseModel):
    message: str
    author: str
