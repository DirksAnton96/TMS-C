from sqlalchemy import select

from models import Note,session

from datetime import datetime

def get_note(uuid: str)->Note:
    with session() as conn:
        query = select(Note).where(Note.uuid==uuid)
        return conn.execute(query).scalar_one()

def create_note(title: str, content: str, time_creation: datetime = datetime.now)->Note:
    with session() as conn:
        note = Note(title=title,content=content,create_at=time_creation)
        conn.add(note)
        conn.commit()
        conn.refresh(note)
    return note

