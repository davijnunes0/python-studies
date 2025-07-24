# Vamos colocar todos os elementos básicos para interagir com nosso meio de persistência de dados.
from src.model.entities.person import Person
from src.database.connection import engine,Base,SessionLocal


class PersonRepository:
    def __init__(self) -> None:
        pass

    def create_database(self) -> None:
        Base.metadata.create_all(bind=engine)
  
    def insert_person(self,person: Person):
        db_session = SessionLocal()
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

        db_session = SessionLocal()
        try:
            person = db_session.query(Person).filter(
                Person._Person__first_name == first_name,
                Person._Person__last_name == last_name
            ).first()
            return person
        finally:
            db_session.close()