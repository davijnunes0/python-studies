class Artista:
    def __init__(self,tipo: str) -> None:
        self.tipo = tipo
    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando seu show")


class Circo:
    def apresentar(self,artista) -> None:
        print("O Circo está abrindo")
        artista.apresentar_show()
        print("O publíco aplaude")
        
