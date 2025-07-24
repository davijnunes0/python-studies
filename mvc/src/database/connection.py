import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"


# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
engine = create_engine(DATABASE_URL, echo=False)

# Cria uma classe 'SessionLocal' que será usada para criar sessões individuais com o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe 'Base' da qual todos os seus modelos ORM herdarão.
# É crucial que todos os modelos usem esta mesma Base.
class Base(DeclarativeBase):
    pass

# (Opcional, mas boa prática) Uma função para obter a sessão e garantir que ela seja fechada.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()