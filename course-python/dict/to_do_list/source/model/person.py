# models.py
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from source.connection.connection_factory import FactoryConnection

class Base(DeclarativeBase):
    pass

    

class Person(Base):
    __tablename__ = "person_tb"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(255))

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="person", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Person(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age})>"

class Task(Base):
    __tablename__ = "task_tb"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    person_id: Mapped[int] = mapped_column(ForeignKey("person_tb.id"))
    person: Mapped["Person"] = relationship(back_populates="tasks")

Base.metadata.create_all(FactoryConnection.create_connection("postgres","12345","db_sales"))

