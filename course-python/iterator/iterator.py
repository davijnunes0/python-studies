def main():
    # Generator expression, Iterables e Iterators em Python
    # Todo generator é um iterator, mas, um iterator não é um generator
    """
     1. O que é um Generator?
         Um generator é uma função que usa yield em vez de return. Quando chamada, ela retorna um objeto generator, que pode ser iterado
         (usando next() ou loops for).
                
    O Que Faz um Generator?
         Pausa a execução: Usa yield para "congelar" a função e retornar um valor.
         Mantém estado: Quando chamado novamente, continua de onde parou.
         lazy: Só processa quando necessário (não carrega tudo na memória).

    Um iterator é um objeto que implementa o protocolo de iteração, que consiste em dois métodos:
         __iter__(): Retorna o próprio objeto iterator.
         __next__(): Retorna o próximo elemento da sequência. Se não houver mais elementos, levanta StopIteration.
"""


    iterable = ["Eu","Tenho","__iter__"]
    iterator = iterable.__iter__()
    print(iterator )

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    print("-=" * 100)

    generator = (x for x in range(20))
    print(next(generator))
    print(next(generator))
    print(next(generator))
   
    print("-=" * 30)

    pause = pause_function(5)
    print(next(pause))
    print(next(pause))
    print(next(pause))
    print(next(pause))
    print(next(pause))
    # Chamada que lança o stop iteration:
    # print(next(pause))

    print("-=" * 100)
    pause_numbers = pause3()
    for number in pause_numbers:
        print(number)



def pause_function(number : int = 0) -> int:
    i : int = 0
    while i < number:
        # Retorna é pausa a execução da função.
        yield i
        i = i + 1
    
    return -1

# Yield from  é usado para delegar a execução de um gerador para outro. Em termos simples,ele permite que um gerador "peça emprestado" os valores de outro gerador, combinando essa sequência de valores.

def pause1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def pause2():
    yield from pause1()
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

def pause3():
    yield from pause2()
    yield 11
    yield 12
    yield 13
    yield 14
    yield 15


if __name__ == "__main__":
    main()
