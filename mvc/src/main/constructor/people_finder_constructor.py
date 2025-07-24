from src.views.people_finder_view import PeopleFinderView
from src.controller.people_register_controller import PeopleRegisterController
from src.controller.people_finder_controller import PeopleFinderController
from src.model.repository.person_repository import PersonRepository
def people_finder_constructor():
    # Criamos um Objeto que guarda o estado é metodos de PeopleFinderView()
    people_finder_view : PeopleFinderView = PeopleFinderView()
    # Criamos um Objeto que guarda o estado é metodos de PersonRepository
    person_repository : PersonRepository = PersonRepository()
    # Criando um Objeto que guarda o estado é metodos de PeopleFinderController()
    people_finder_controller: PeopleFinderController = PeopleFinderController(person_repository)
    # Pegamos os dados da pessoa que queremos procurar.
    person_information : dict[str,str] = people_finder_view.find_person_view()
    # Passando os dados da pessoa para o controller
    response : dict = people_finder_controller.find_by_name(person_information)

    if response["sucess"]:
        people_finder_view.find_person_sucess(response["message"])
    else:
        people_finder_view.find_person_fail(response["error"])