def main():

    print("hello world")
    x,y,*resto = 1,2,3,4
    print(x,y,resto)
    print(*resto)
    
    print(sum_(1,2,3,4,5))
    print(multiplication(1,2,3,4,5))
    print(is_eveen(3))
    print(is_eveen(2))

def sum_(*args: tuple[int]) -> int:
    total: int = 0

    for number in args:
        total += number
    
    return total



def multiplication(*args) -> int:

    total : int = 1
    i : int = 0

    while i < len(args):
        total = total * args[i]
        i += 1

    return total


def is_eveen(number : int) -> str:

    return "Eveen" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    main()
