def main():
    """
       >>> sum_more_five(10)
       15
       >>> multiple_per_teen(2)
       20
    """
    sum_more_five =  run(sum_n,5)
    multiple_per_teen = run(multiple_n,10)

    print(sum_more_five(10))
    print(multiple_per_teen(2))

 # Usando closure porque a funtion sum_with_n vai ter que "lembrar" do (x) da function sum_n
def sum_n(x: int) -> int:
    def sum_with_n(y: int):
        return x + y

    return sum_with_n

# Usando closure porque a function multiple_with_n vai ter que "lembrar" de (x) da function multiple_n
def multiple_n(x: int) -> int:
    def multiple_with_n(y: int):
        return x * y

    return multiple_with_n


def run(func:callable, *args) -> None: return func(*args)

if __name__ == "__main__":
    main()
