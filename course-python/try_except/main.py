"""
Erros durante a execução são abordados e não necessariamente fatais: logo veremos como tratá-los em programas Python. A maioria das abordagens
não são tratadas pelos programas e terminam em mensagem de erro:

Em Python exceções são classes herdadas da superclasse Exception()

"""

def main():
    
   response = check_division(get_number("X: "), get_number("Y: "))
   
   if response["sucess"]:
        print(response["response"])
   else:
        print(response["error"])

   print("-=")

   try:
       check_string("")
       check_string(10)
   except ValueError as error:
        print(error.__class__.name)
   except TypeError as error:
        print(error.__class__.name)



def check_division(x: float, y: float) -> float:

    try:
        response = {"sucess": True,"response": x / y}
        return response
    except ZeroDivisionError as e:
        return {"sucess": False,"error": e.__class__.__name__}
    finally:
        print("Bloco utilizado para fechamento de recursos,pois, será executado tanto se ocorrer um erro é se não ocorrer um erro")

def check_string(string: str) -> None:

    if not isinstance(string,str):
        # Estamos lançando uma exceção caso o argumento enviado para o parâmetro string não for uma str()
        raise TypeError("A string deveria ser do tipo str()")

    if len(string) <= 0:
        # Estamos lançando uma exceção caso a string não tenha a quantidade de caracteres correta.
        raise ValueError("A string está vazia")

def get_number(prompt: str) -> int:
    """
    A instrução try funciona das seguintes maneiras:

    1- Se nenhuma exceção ocorrer,a cláusula exceto é ignorada e a excução da instrução try é finalizada.

    2- Se ocorrer uma exceção durante a execução de uma cláusula try, conforme as instruções exigidas na
    cláusula são ignoradas. Se o tipo de exceção de corrida tiver sido previsto em algum except, essa cláusula
    exceto é reliazada,e então depois a execução continua após o bloco try/except.

    3- Se a exceção criada não representa nenhuma exceção listada na cláusula da exceção, então ela é entregue a uma instrução try mais 
    externa. Se não exisitr nenhum tratado previsto para tal exceção, trata-se de uma exceção não tratada e a exceução do programa termina com
    uma mensagem de erro.

    """

    while True:
       try:
            return int(input(prompt))
       except ValueError:
            print("Ops! Esse não é um número válido. Tente novamente...")


if __name__ == "__main__":
    main()
