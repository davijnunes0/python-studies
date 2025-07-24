from src.views.people_register_view import PeopleRegisterView
from src.controller.people_register_controller import PeopleRegisterController

def people_register_constructor():
    # Criamos um Objeto que armazena os estados é metodos da classe PeopleRegisterView().
    people_register_view :  PeopleRegisterView = PeopleRegisterView()  
    # Criamos um objeto que armazena os estados é metodo da classe PeopleRegisterController
    people_register_controller : PeopleRegisterController = PeopleRegisterController()
    # Pegamos as informações retornadas pela view.
    new_person_information : dict[str,str] = people_register_view.register_person_view()
    # Passamos os dados da view <-> para o controller para cadastrar a pessoa.
    response : dict = people_register_controller.register(new_person_information)
    # Pegamos a resposta do controler para mostrar na view
    if response["sucess"]:
        people_register_view.register_person_sucess(response["message"])    
    else:
        people_register_view.register_person_fail(response["error"])