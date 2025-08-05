class Interruptor:
    def __init__(self,comodo: str) -> None:
        self.__comodo = comodo

    def set_comodo(self,comodo : str) -> None | ValueError:
        if comodo:
            self.__comodo = comodo
        else:
            raise ValueError("Valor de comodo é inválido")

    def get_comodo(self) -> str:
        return self.__comodo
    
    def acender(self):
        print(f"{self.__comodo} está com  a luz acessa")

    def apagar(self):
        print(f"{self.__comodo} está com a luz apagada")
