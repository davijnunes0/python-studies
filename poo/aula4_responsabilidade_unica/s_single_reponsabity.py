

class CadastralSystem:
    def cadastrar(self,first_name : str,last_name : str, age: int) -> None:
        # Validar os dados:
        response : bool =  self.__validate_input(first_name,last_name,age)
        if response:
            # Pegar conexão com banco de dados
            self.__get_connection()
            # Cadastrando o usuário no banco de dados 
            self.__register_user(first_name,last_name,age)
        # Caso ocorra algum erro nos dados do usuário
        else:
            self.__error_handle()


    def __validate_input(self,first_name : str, last_name: str, age: int) -> None:

        validate_fields : bool =  isinstance(first_name,str) and isinstance(last_name,str) and isinstance(age,int)
        return validate_fields

    def __get_connection(self):
        print("Pegando conexão com banco de dados")

    def __register_user(self,first_name,last_name,age: int) -> None:
        print(f"Cadastrando o usuário: {first_name}, {last_name}, age= {age}")

    def __error_handle(self) -> ValueError:
        raise ValueError("Usuário inválido")
