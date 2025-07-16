def main():


    persons = [
     {"name" : "julia","age" : 50},
     {"name" : "Maria" ,"age" : 20},
     {"name" : "Yasmin","age" :  40}
     ]
    
    print(persons)
    persons.sort(key= lambda person : person["age"])

    print("-=" * 100)
    print(persons)

    print("-=" * 100)

    print(
        run(lambda x,y : x + y,2,3),
        run(sum_,2,3)
    
    )

    print("-=" * 100)

    double = run(
        lambda m : lambda n : m * n,2

     )

    print(double(5))


def run(function,*args):
    return function(*args)

def sum_(x : int, y : int) -> int:
    return x + y

def multiplicador(multiplicator_number : int):
    def multiplicator(number):
        return multiplicator_number * number
    return multiplicator

if __name__ == "__main__":
    main()
