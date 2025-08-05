from phone import Phone

class Person:
    def __init__(self,phone: Phone) -> None:
        self.__phone = phone
    
    def set_phone(self,phone: Phone) -> None | ValueError:
        if phone:
            self.__phone = phone
        else:
            raise ValueError("Value phone is invalid")

    def get_phone(self) -> Phone:
        return self.__phone

    def pedir_pizza(self):
        print("Pedindo")
        self.__phone.send_message("Quero uma pizza de calabresa")

    def estudar(self):
        print("Estudando..")
        self.__phone.open_youtube()
