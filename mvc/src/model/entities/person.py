import sqlalchemy
from sqlalchemy import create_engine, String,Integer,Float
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker
from src.database.connection import Base

# 2. Mapear a classe person:
class Person(Base):
    
    # Nome na tabela no banco de dados
    __tablename__ = "tb_person"
    
    # Mapeando as colunas DIRETAMENTE para os atributos com __
    id: Mapped[int] = mapped_column(primary_key=True)
    __first_name: Mapped[str] = mapped_column("first_name",String(50))
    __last_name: Mapped[str] = mapped_column("last_name",String(50))
    __age: Mapped[Integer] = mapped_column("age",Integer)
    __heigth: Mapped[Float] = mapped_column("heigth",Float)

    

    def __init__(self,first_name : str, last_name : str, age: int, heigth: float) -> None:
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_age(age)
        self.set_heigth(heigth)


    def set_first_name(self,first_name : str) -> None:
        if isinstance(first_name,str):
            self.__first_name = first_name
        else:
            raise ValueError("First name is invalid.")
        
    def get_first_name(self) -> str: return self.__first_name
    
    def set_last_name(self,last_name : str) -> None:
        if isinstance(last_name,str):
            self.__last_name = last_name
        else:
            raise ValueError("Last name is invalid.")
        
    def get_last_name(self) -> str: return self.__last_name

    def set_age(self,age: int) -> None:
        if isinstance(age,int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age is invalid.")
    
    def get_age(self) -> int: return self.__age

    def set_heigth(self,heigth: float) -> None:
        if isinstance(heigth,float) and heigth > 0.0:
            self.__heigth = heigth
        else:
            raise ValueError("Heigth is invalid.")

    def get_heigth(self) -> float: return self.__heigth
