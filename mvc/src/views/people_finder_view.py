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