from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from model.person import Person
from source.connection.connection_factory import FactoryConnection

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "task_tb"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50),nullable=False)
    description: Mapped[str] = mapped_column(String(50),nullable=False)
    person_id : Mapped[int] = mapped_column(ForeignKey("person_tb.id"))
    person : Mapped["Person"] = relationship("Person",back_populates="task_tb")

Base.metadata.create_all(FactoryConnection.create_connection("postgres","12345","db_sales"))
