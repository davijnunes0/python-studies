from src.views.people_finder_view import PeopleFinderView
from src.controller.people_register_controller import PeopleRegisterController

def people_finder_constructor():
    # Criamos uma instância da view.
    people_finder_view : PeopleFinderView = PeopleFinderView()
    # Pegamos os dados da pessoa que queremos procurar.
    person_information : dict[str,str] = people_finder_view.find_person_view()
   