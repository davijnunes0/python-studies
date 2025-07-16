from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/db_sales"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# @Entity
class Films(Base):
    __tablename__ = "films"
    title: Mapped[str] = mapped_column(primary_key=True)
    genre: Mapped[str] = mapped_column(String(30),nullable=False)
    year: Mapped[int] = mapped_column(Integer,nullable=False)

    def __repr__(self):
        return f"Filme (titulo={self.title!r}, genero={self.genre!r}, ano={self.year!r})"

# @Entity
class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    def __repr__(self):
        return f"Ator(id={self.id!r}), name={self.name!r}, fullname={self.fullname!r}"

# Create table in DATABASE
Base.metadata.create_all(engine)


