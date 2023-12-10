import uuid
from sqlalchemy import Column, String,DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

connection_string = "mysql+mysqlconnector://root:admin123@192.168.218.77:8306/test"

engine = create_engine(connection_string, echo=True)

session = sessionmaker(bind=engine, autoflush=False)


if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()

session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"
    uuid = Column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))
    title = Column(String(64),unique=True, nullable=False)
    content = Column(String(500), nullable=False)
    create_at = Column(DateTime, default = datetime.now)

def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)

def add_notes():
    with session as conn:
        conn.add(Note(title="Text",content="Hello world!"))
        conn.commit