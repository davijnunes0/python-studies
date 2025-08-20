from sqlalchemy import Column, DateTime,Integer, String,func,create_engine,MetaData,select
from sqlalchemy.orm import DeclarativeBase,Session
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
    
    def __repr__(self):
        """
        Retorna uma representação de string oficial do objeto,
        útil para depuração.
        """
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"live={self.live!r}"
            f")>"
        )


Base.metadata.create_all(engine)


with Session(engine) as session:
    # hello_comment = Comment(name="hello",comment="hello Julia",live="sksksksksks")
    # session.add(hello_comment)
    # session.commit()

    stmt = select(Comment)
    for person in session.scalars(stmt):
        print(person)