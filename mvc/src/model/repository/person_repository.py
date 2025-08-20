# Vamos colocar todos os elementos básicos para interagir com nosso meio de persistência de dados.
from src.model.entities.person import Person
from src.database.connection import engine,Base
from sqlalchemy.orm import Session


class PersonRepository:
    def __init__(self) -> None:
        pass

    def create_database(self) -> None:
        Base.metadata.create_all(bind=engine)
  
    def insert_person(self,person: Person):
        with Session(engine) as db_session:
            try:
                db_session.add(person)
                db_session.commit()
                db_session.refresh(person)
            except Exception as e:
                db_session.rollback()
                raise e
            finally:
                db_session.close()


    def find_person_by_name(self,first_name: str,last_name: str) -> Person | None:
        with Session(engine) as db_session:
            try:
                person = db_session.query(Person).filter(
                    Person.first_name == first_name,
                    Person.last_name == last_name
                ).first()
                return person
            except Exception as exception:
                raise exception

    
    # Método para atualizar dados de uma pessoa.
    def update_person(self,person_data: dict):
       with Session(engine) as db_session:
           # Pegando o id da pessoa é convertendo para inteiro
           id_person = int(person_data["id_person"])
           #1. Usando session.get() para buscar pela primary key
           db_person = db_session.get(Person,id_person)
           #2. Verificando se a pessoa foi encontrada
           if not db_person:
               raise ValueError(f"Pessoa com ID {id_person} não encontrada.")

           #3. Atualizando os campos do objeto encontrado no banco de dados
           db_person.first_name =  person_data["first_name"]
           db_person.last_name = person_data["last_name"]
           db_person.age = person_data["age"]
           db_person.heigth = person_data["heigth"]

           # 4. Commitando a transação O "with" já cuida do rollback em caso de erro
           db_session.commit()

    

    # Método Delete person
    def delete_person(self,person_data: dict):
        with Session(engine) as db_session:
            # Pegando o id da pessoa é convertendo para inteiro
            id_person = int(person_data["id_person"])
            #1. Usando o session.get() para buscar pela primay key
            db_person = db_session.get(Person,id_person)
            #2. Verificando se a pessoa foi encontrada
            if not db_person:
               raise ValueError(f"Pessoa com ID {id_person} não encontrada.")
            
            # Deletando a pessoa do banco de dados
            db_session.delete(db_person)

            # Commitando a transação
            db_session.commit()