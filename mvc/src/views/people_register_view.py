import os
from typing import Dict
import pprint

class PeopleRegisterView(object):
    
    def register_person_view(self) -> Dict[str,str]:
        os.system("clear")
        print("Digite os dados da pessoa que deseja cadastrar: ")
        first_name : str = input("First name: ").strip().title()
        last_name : str = input("Last name: ").strip().title()
        age : str = input("Age: ").strip()
        heigth : str = input("Heigth: ").strip()

        return {
            "first_name" : first_name,
            "last_name" : last_name,
            "age": age,
            "heigth" : heigth
        }
    

    def register_person_sucess(self,message : Dict) -> None:
        os.system("clear")

        sucess_message  : str = f"""
            Pessoa cadastrado com sucesso!
            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                first_name: {message["attributes"]["first_name"]}
                last_name: {message["attributes"]["last_name"]}
                age: {message["attributes"]["age"]}
                heigth: {message["attributes"]["heigth"]}
        """

        print(sucess_message)

    def register_person_fail(self,error: str) ->  None:
        os.system("clear")

        fail_message : str  = f"""
            Falha ao cadastrar o usuário
            Error: {error}
        """
    
        print(fail_message)