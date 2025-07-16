def main():

    A : set[int] = {1,2,3,4,5,6,7,8,8,9,10}
    B : set[int] = {1,2,3,4,5,6,11,12,13,14,15}
    print(A,B)
    print(type(A),type(B))
    print("-=" * 300)

    A.add(20)
    A.add(30)
    print(A)

    print("-=" * 300)

    print(A & B) # intersection
    print(A.union(B)) # unio
    print(A - B) # difference
    print(A ^ B) # symmetric difference

    print("-=" * 300)
    lista_de_listas_de_inteiros =  [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

    ]


    i : int = 0

    while i < len(lista_de_listas_de_inteiros):
        
        repetead_number : int = get_the_first_repetead_number(lista_de_listas_de_inteiros[i])
        print(repetead_number)
        i += 1

def get_the_first_repetead_number(list_of_numbers: list[int]) -> int:

    seen : set[int] = set()


    for number in list_of_numbers:
        if number in seen:
            return number
        seen.add(number)
    
    return -1

if __name__ == "__main__":
    main()      
