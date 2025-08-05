def main():
    
    value_float : float = get_value_float("Enter a farenheit: ")
    F : float = conversion(value_float)
    # Output
    print(f"Celsius: {F}")

    print("-=" * 100)
    print(__name__)

    print("-=" * 100)
    
    print(help(conversion))



# Input
def get_value_float(prompt : str) -> float:
    """ Retorna uma valor de ponto flutuante.
    Args:
        prompt (str): Mensagem que irá aparecer no input();
    Returns:
        Float: Um valor float;
    Raise:
        ValueError: Se o número digitado pelo usuário não for um número de ponto flutuante;

    """
    try:
        return float(input(prompt))
    except ValueError as e:
        print(f"Error: {e}")

# Processamento
def conversion(farenheit: float) -> float:
    """ Retorna a temperatura em celsius
    Args:
        farenheit (float): Temperatura em farenheit.
    Returns:
        Float: Retorna a temperatura em celsius:
    Raise:
        ValueError: Se o número digitado pelo usuário for um valor inválido.

    >>> conversion(32)
    0.0
    >>> conversion(-40)
    -40.0
    >>> conversion(32)
    1.1
    """
    try:
        celsius: float = 5 * ((farenheit - 32) / 9)
        return celsius
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
