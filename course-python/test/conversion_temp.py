def main():
    
    convert_temperature : float = calculation_temperature()
    
    print(f"Temperature: {convert_temperature}")


def calculation_temperature() -> float:
    
    
    option: str = get_option_temperature()
    temperature: float = get_value_float("Enter a temperature: ")

    if option.lower() == "c":
        return conversion_to_farenheit_to_celsius(temperature)

    return conversion_to_celsius_to_farenheit(temperature)


def get_option_temperature() -> str:
    """Função responsável por pegar qual temperatura o usuário quer.
       returns:
            Retorna a temperatura deseja pelo usuário.
    """


    while True:
        response : str = input("Digite (c/f): ")
        if response.lower() == "c" or response.lower() == "f":
            return response


def get_value_float(prompt : str) -> float:
    """Função responsável por receber um número de ponto flutuante válido.
      args:
        prompt é a frase que irá aparecer para o usuário digitar a entrada.

    """
    try:
        return float(input(prompt))
    except ValueError as e:
        print(f"Error: {e}")


def conversion_to_farenheit_to_celsius(temperature: float) -> float:
    """Função responsável por converter farenheit em celsius.
       args:
          temperature é a temperatura que irá ser convertida.
       returns:
          A temperatura convertida em celsius é retornada.

       >>> conversion_to_farenheit_to_celsius(32)
       0.0
       >>> conversion_to_farenheit_to_celsius(-40)
       -40.0
    """
    return 5 * ((temperature - 32) / 9)

def conversion_to_celsius_to_farenheit(temperature: float) -> float:
    """Função responsável por converter celsius em farenheit.
        args:
            tempeture é a temperatura que irá ser convertida.
        returns:
            A temperatura convertida em farenheit é retornada.0

    """
    return temperature * (9 / 5) + 32


if __name__ == "__main__":
    main()
