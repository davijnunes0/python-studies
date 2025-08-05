# Estrutura que agrupa um conjunto de métodos é atributos,
# Um objeto é uma instância de uma classe que armazena estados e métodos.
# self representa a instância atual que estamos lidando.
class MyClass:

        def __init__(self,value: float, item: str):
          self.__value = value
          self.__item = item

        def setter_value(self,value) -> None:
            if value:
                self.__value = value
            else:
                raise ValueError("Value is invalid")

        def getter_value(self) -> float:
            return self.__value

        def setter_item(self,item: str) -> None:
            if item:
                self.__item = item
            else:
                raise ValueError("Item is invalid")

        def getter_item(self) -> str:
            return self.__item
        
