"""
Desempacotar o dicionário significa "espalhar" seus pares chave-valor em um novo contexto.
Os dois usos mais comuns são para unir dicionários e para passar agumentos nomeados para uma função.
"""
def main():
    print()

    person_data : dict = {"name" : "Davi", "age": 20}
    major : dict = {"major" : "Computer science"}
    person = {**person_data,**major}
    print(person)

    print()
    
    data  : dict = {"title" : "Pagamento", "author" : "Julia"}
    criar_relatorio(**data)

    print("-=" * 100)
    print_kwargs(**data)


"""
Você pode usar **  para desempacotar um dicionário e passar seus itens como argumentos nomeados (keyword arguments) para uma função.
As chaves do dicionário devem corresponder aos nomes dos parâmetoros da função.
"""

def criar_relatorio(title,author,version=1.0):
    print(f"--- Relatório: {title} ---")
    print(f"--- Author: {author} ---")
    print(f"--- Version: {version} ---")

"""
2. Empacotamento de Dicionários (**kwargs)
Empacotar é o processo inverso. Acontece na definição de uma função e serve para coletar um número arbitrario de argumentos nomeados em um único dicionário. A convenção é chamar esse dicionário de kwargs (de keyword arguments).
"""

def print_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

if __name__ == "__main__":
    main()
