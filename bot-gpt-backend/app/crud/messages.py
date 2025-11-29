from sqlalchemy.orm import Session
from app.models import Message

def add_message(db: Session, conv_id: int, role: str, content: str):
    msg = Message(conversation_id=conv_id, role=role, content=content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def get_messages(db: Session, conv_id: int):
    return (
        db.query(Message)
          .filter(Message.conversation_id == conv_id)
          .order_by(Message.id)
          .all()
    )
