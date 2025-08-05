class Phone:
    def __init__(self,model: str) -> None:
        self.__model = model

    def set_model(self,model: str) -> None | ValueError:
        if model:
            self.__model = model
        else:
            raise ValueError("Valor de model inválido")

    def get_model(self) -> str:
        return self.__model

    def send_message(self,message: str) -> None:
        print(message)

    def open_emails(self):
        print("Abrindo emails")

    def open_youtube(self):
        print("Abrindo youtube")
