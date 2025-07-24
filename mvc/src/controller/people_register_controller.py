from typing import Dict

class PeopleRegisterController:

    def __init__(self) -> None:
        pass

    def register(self,new_person_informations: Dict) -> Dict:
        try:
            # Método para validar os dados.
            self.__validate_fields(new_person_informations)
            # Enviar para  models para cadastro de dados
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