from sqlalchemy.orm import Session
from app.models import Conversation

def create_conversation(db: Session):
    conv = Conversation()
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conv

def list_conversations(db: Session):
    return db.query(Conversation).all()

def get_conversation(db: Session, conv_id: int):
    return db.query(Conversation).filter(Conversation.id == conv_id).first()

def delete_conversation(db: Session, conv_id: int):
    conv = get_conversation(db, conv_id)
    if conv:
        db.delete(conv)
        db.commit()
    return True
