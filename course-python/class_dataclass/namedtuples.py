from collections import namedtuple
from person import Person

# 1. Definindo a estrutura da nemedtuple
# O primeiro argumento é o nome da "classe"
# O segundo é uma string com os nomes dos campos, separados por espaço.

def main():
    
    person = namedtuple("Person","nome sobrenome telefone ddd")
    
    dados = [
        person("Davi","Nunes",{"residencial" : "1111-111","móvel":"999-999-999"},19)
    ]

    davi  = dados [0]
    print(davi.nome)
    print(davi.sobrenome)
    print(davi.telefone)
    print(davi.ddd)

    print("-=" * 100)
    julia = Person("Julia","Pinheiro",{"residencia": "2222-222","móvel":"999-999-999"},62)
    print(julia)


if __name__ == "__main__":
    main()
