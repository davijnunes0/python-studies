from sqlalchemy import Column, DateTime,Integer, String,func,create_engine,MetaData
from sqlalchemy.orm import DeclarativeBase

# Schemas / Types

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"

# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
# Isso é uma fabrica de conexão.

engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()


class Base(DeclarativeBase):
    ...

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    live = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

Base.metadata.create_all(engine)