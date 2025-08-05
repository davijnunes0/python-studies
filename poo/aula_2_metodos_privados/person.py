# Demonstrando um dos pilares da OO -> Encapsulamento.
# Em python em tese não existe encapsulamento.
class Person:
    def __init__(self,heigth: float, cpf: str) -> None:
        self.heigth = heigth
        self.__cpf = cpf

    def hello(self):
        print(f"hello! my heigth: {self.heigth}")
        self.__recover_document()

    def __recover_document(self):
        print(f"My document: {self.__cpf}")

