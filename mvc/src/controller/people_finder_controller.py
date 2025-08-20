from typing import Dict
from src.model.repository.person_repository import PersonRepository
from src.model.entities.person import Person

class PeopleFinderController:
    def __init__(self,person_repository: PersonRepository):
        self.person_repository = person_repository

    def find_by_name(self,person_finder_informations: Dict) -> Dict:
        try:
            # Método que valida os campos do dicionário => person_finder_informations.
            self.__validate_fields(person_finder_informations)
            # Método que busca o usuário no banco de dados.
            person : Person =  self.person_repository.find_person_by_name(first_name=person_finder_informations["first_name"],
            last_name=person_finder_informations["last_name"])
            response = self.__format_response(person)
            return {"sucess" : True,"message": response}
        except Exception as exception:
            return {"sucess": False,"error" : str(exception)}
    
    def __validate_fields(self,person_finder_informations: Dict) -> None:
        if not isinstance(person_finder_informations["first_name"],str):        
            raise ValueError("First name is invalid.")
        if not isinstance(person_finder_informations["last_name"],str):
            raise ValueError("Last name  is invalid.")
    

    def __format_response(self,person: Person) -> Dict:
        return {
            "count" : 1,
            "type" : "Person",
            "infos":{
                "first_name" : person.first_name,
                "last_name" : person.last_name
            }
        }
    