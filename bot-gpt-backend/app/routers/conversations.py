from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import *
from app.crud import conversations as crud_conv, messages as crud_msg
from app.llm_service import call_llm

router = APIRouter(prefix="/conversations")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ConversationOut)
def start_conversation(payload: ConversationCreate, db: Session = Depends(get_db)):
    conv = crud_conv.create_conversation(db)
    crud_msg.add_message(db, conv.id, "user", payload.first_message)

    ai_reply = call_llm([{"role": "user", "content": payload.first_message}])
    crud_msg.add_message(db, conv.id, "assistant", ai_reply)

    messages = crud_msg.get_messages(db, conv.id)
    conv.messages = messages
    return conv


@router.get("/", response_model=list[ConversationOut])
def list_all(db: Session = Depends(get_db)):
    convs = crud_conv.list_conversations(db)
    for c in convs:
        c.messages = crud_msg.get_messages(db, c.id)
    return convs


@router.get("/{conv_id}", response_model=ConversationOut)
def get_one(conv_id: int, db: Session = Depends(get_db)):
    conv = crud_conv.get_conversation(db, conv_id)
    conv.messages = crud_msg.get_messages(db, conv_id)
    return conv
