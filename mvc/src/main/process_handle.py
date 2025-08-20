from .constructor.introduction_process import introduction_process
from .constructor.people_finder_constructor import people_finder_constructor
from .constructor.people_register_constructor import people_register_constructor
from .constructor.people_register_constructor import people_update_constructor
# .constructor a partir do diretório onde está o arquivo process_handle.py encontre a pasta .constructor

def start() -> None:
    while True:
        command : str = introduction_process()
        if command == "1":
            people_register_constructor()
        elif command == "2":
            people_finder_constructor()
        elif command == "3":
            people_update_constructor()
        elif command == "4":
            exit("Saindo do programa")
        else:
            print("\n Comando inválido.)")

        