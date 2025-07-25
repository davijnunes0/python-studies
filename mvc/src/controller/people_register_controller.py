from typing import Dict
from src.model.entities.person import Person
from src.model.repository.person_repository import PersonRepository

class PeopleRegisterController:

    def __init__(self,person_repository: PersonRepository) -> None:
        self.person_repository = person_repository

    def register(self,new_person_informations: Dict) -> Dict:
        try:
            # Método para validar os dados.
            self.__validate_fields(new_person_informations)
            # Cria o objeto Person()
            person : Person = self.__build_person(new_person_informations)
            # Enviar para  o repository para cadastrar a pessoa
            self.person_repository.insert_person(person)
            # Retorna a resposta para view de uma maneira formatada é concisa.
            response = self.__format_response(new_person_informations)
            return {"sucess" : True,"message" : response}
        except Exception as exception:
            return {"sucess" : False,"error" : str(exception)}
    def __validate_fields(self,new_person_informations: Dict) -> None:
        
        # Valida o primeiro nome da pessoa.
        if not isinstance(new_person_informations["first_name"],str):
            raise Exception("First name is invalid!")

        # Valida o sobrenome da pessoa.
        elif not isinstance(new_person_informations["last_name"],str):
            raise Exception("Last name is invalid!")
        
        # Valida a idade da pessoa.
        try:
            int(new_person_informations["age"])
        except:
            raise ValueError("Field age is invalid")
        
        # Valida a altura da pessoa.
        try:
            float(new_person_informations["heigth"])
        except:
            raise ValueError("Field heigth is invalid!")
    
    def __format_response(self,new_person_informations: Dict) -> Dict:
        return{
            "count" : 1,
            "type" : "Person",
            "attributes" : new_person_informations
        }
    
    def __build_person(self,new_person_informations) -> Person:
        return Person(first_name=new_person_informations["first_name"],
                      last_name=new_person_informations["last_name"],
                      age=int(new_person_informations["age"]),
                      heigth=float(new_person_informations["heigth"])
                      )