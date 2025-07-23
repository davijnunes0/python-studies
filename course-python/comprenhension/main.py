"""
List comprehension é uma forma concisa,legível e eficiente  de criar listas em Python. Ela permite que você gere uma nova lista aplicando uma
expressão a cada item de uma sequência existente, com a opção de filtrar os itens que serão incluidos.

sintaxe : list = [expression for expression in iterable if condition]

"""

import pprint

def main():
    print()

    double = lambda n : n * 2
    double_even_numbers : list[int] = [double(x) for x in range(10) if x % 2 == 0]
    print(double_even_numbers)

    print("-=" * 100)

    products : lisct[dict] = [
        {"name" : "Smartphone","price": 2000.00},
        {"name": "Videogame","price": 4000.00},
        {"name": "Computer", "price" : 5000.00}
            ]

    pprint.pprint(products)

    print("-=" * 100)

    new_products : list[dict] = [
        # Mapeamento dos produtos!
        {**product,"price" :  product["price"] + product["price"] * 0.05}
        # Mapemanto utilizando a cláusula if ternária!
        if product["price"] > 2000 else {**product}
        for product in products
        # filtrando produtos!
        if product["price"] + product["price"] * 0.05 > 2100
    ]

    pprint.pprint(new_products)

    print("-=" * 100)

    matrix : list[list[int]] = [
            
                [0,0,0] 
                for x in range(3)
            ]

    print(matrix)
    print("-=" * 100)

    # Dictionary comprenhension
    number = { x : x * 2 for x in range(10)}
    print(number)

    print("-=" * 100)

    # Set comprenhesion
    sets = {x for x in range(10)}
    print(sets)

    print()
    
    print(is_number(50))
    print(is_number(50.00))


def is_number(number: int) -> bool:
    # Verifica se number é um número do tipo float() ou é do tipo int()
    return isinstance(number,(float,int))
       

if __name__ == "__main__":
    main()
