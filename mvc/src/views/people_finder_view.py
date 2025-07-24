from typing import Dict
import os

class PeopleFinderView(object):
    def __init__(self):
        pass
    
    # Método responsável por exibir a tela de buscar pessoas
    # Retorna um dicionário com os dados da pessoa a ser buscada
    def find_person_view(self) -> Dict[str,str]:
        os.system("clear")
        print("Digite o nome da pessoa que deseja encontrar: ")
        first_name : str = input("First name: ").strip().title()
        last_name  : str = input("Last name: ").strip().title()
        return {"first_name": first_name,"last_name": last_name}

    def find_person_sucess(self,message: Dict) -> None:
        os.system("clear")
        sucess_message : str = f"""
            Usuário encontrado com sucesso!
            Tipo: {message["type"]}
            Registros: {message["count"]}
            "Infos":
                First Name: {message["infos"]["first_name"]}
                Last Name: {message["infos"]["last_name"]}
        """

        print(sucess_message)
    
    def find_person_fail(self,error: str) -> None:
        os.system("clear")
        fail_message = f"""
            Falha ao encontrar a pessoa!
            Error: {error}
        """
        print(fail_message)