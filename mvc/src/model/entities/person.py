import sqlalchemy
from sqlalchemy import Column,Integer,String,Float
from src.database.connection import Base

# 2. Mapear a classe person:
class Person(Base):
    
    # Nome na tabela no banco de dados
    __tablename__ = "tb_persons"

    # Atributos que serão mapeados para formar uma entidade no banco de dados
    id = Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    heigth = Column(Float,nullable=False)

    def __init__(self,first_name : str, last_name : str, age: int, heigth: float) -> None:
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      self.heigth = heigth