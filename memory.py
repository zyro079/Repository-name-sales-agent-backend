from database import SessionLocal
from models import Conversation


def save_message(user_id, role, message):
    db = SessionLocal()

    msg = Conversation(
        user_id=user_id,
        role=role,
        message=message
    )

    db.add(msg)
    db.commit()
    db.close()


def get_history(user_id):
    db = SessionLocal()

    messages = db.query(Conversation).filter(
        Conversation.user_id == user_id
    ).all()

    db.close()

    return messages


def clear_memory(user_id):
    db = SessionLocal()

    db.query(Conversation).filter(
        Conversation.user_id == user_id
    ).delete()

    db.commit()
    db.close()