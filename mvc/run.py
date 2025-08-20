from src.main.process_handle import start
from src.model.repository.person_repository import PersonRepository
from src.model.entities.person import Person

def main() -> None:

    pass
if __name__ == "__main__":
    person_repository: PersonRepository = PersonRepository()
    person_repository.create_database()
    """
    person_repository.update_person(
        {"id_person": 1, 
         "first_name": "Davi",
         "last_name": "José",
         "age": 21,
         "heigth": 1.902

     })
    """
    
    """
    person_repository.delete_person(
        {"id_person": 4, 
         "first_name": "Davi", 
         "last_name": "Nunes", 
         "age": 20, 
         "heigth": 20})
    """

    start()
    