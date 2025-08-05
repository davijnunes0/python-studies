from copy import deepcopy

def main():
    
    products : listt[dict,dict] = [
                {"name" : "Product 5","price": 10.00},
                {"name": "Product 1","price": 23.32},
                {"name" : "Product 3","price":  10.11},
                {"name" : "Product 2","price" : 105.87},
                {"name": "Product 4", "price" : 69.50}
            ]

    # Aumentando o preço dos produtos
    new_products : list[dict,dict] = increase_percent_value_product(products)
    print_product(new_products)
    
    print("-=" * 100)
    # Ordenando pelo nome do produto de forma descrescente
    new_products.sort(key=lambda product : product["name"], reverse=True)
    print("Products in descending order:")
    print_product(new_products)
    print("-=" * 100)
    
    # Fazendo a cópia profunda
    products_order_by_name : list[dict,dict] = deepcopy(new_products)
    print_product(new_products)

    print("-=" * 100)
    # Ordenando pelo preço do produto de forma crescente
    new_products.sort(key=lambda product : product["price"],reverse=False)
    print("Products in ascending order:")
    print_product(new_products)
    print("-=" * 100)
    
    # Fazendo a cópia profunda
    products_order_by_price : list[dict,dict] = deepcopy(new_products)
    print_product(products_order_by_price)
    

def increase_percent_value_product(products: list[dict,dict]) -> list[dict,dict]:

    new_products : list[dict,dict] = [
            {**product,"price" : product["price"] + product["price"] * 0.1} 
                for product in products
            ]

    return new_products


def print_product(products: list[dict,dict]) -> None:

    for product in products:
        print(product)


if __name__ == "__main__":
    main()
