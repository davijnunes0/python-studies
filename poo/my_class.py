class Person:
    # Self se refere a instância atual da classe"
    # Método responsável por inicializar a classe
    def __init__(self, first_name: str,last_name : str, age: int) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self,first_name) -> None:
        if first_name:
            self.__first_name = first_name
        else:
            raise ValueError("First name is invalid")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self,last_name) -> None:
        if last_name:
            self.__last_name = last_name
        else:
            raise ValueError("Last name is invalid")

    @property
    def age(self) -> int:
        return self.__age

