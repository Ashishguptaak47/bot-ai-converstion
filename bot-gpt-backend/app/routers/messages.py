from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import messages as crud_msg, conversations as crud_conv
from app.llm_service import call_llm
from app.schemas import MessageCreate

router = APIRouter(prefix="/messages")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{conv_id}")
def send_message(conv_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    crud_msg.add_message(db, conv_id, "user", msg.content)

    history = [{"role": m.role, "content": m.content}
               for m in crud_msg.get_messages(db, conv_id)]

    assistant_reply = call_llm(history)

    crud_msg.add_message(db, conv_id, "assistant", assistant_reply)

    return {"reply": assistant_reply}
