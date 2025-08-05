from interruptor import Interruptor

class Pessoa:
    def __init__(self,interruptor: Interruptor) -> None:
        self.__interruptor = interruptor

    def apagar_luz(self):
        self.__interruptor.apagar()

    def acender_luz(self):
        self.__interruptor.acender()

    def dormir(self):
        self.__interruptor.apagar()
        print("Estou indo domir")
