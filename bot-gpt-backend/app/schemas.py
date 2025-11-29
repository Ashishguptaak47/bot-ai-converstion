from pydantic import BaseModel
from typing import List

class MessageCreate(BaseModel):
    role: str
    content: str

class MessageOut(BaseModel):
    id: int
    role: str
    content: str

    class Config:
        orm_mode = True


class ConversationCreate(BaseModel):
    first_message: str

class ConversationOut(BaseModel):
    id: int
    title: str
    messages: List[MessageOut]

    class Config:
        orm_mode = True
