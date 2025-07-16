def main():
    
    greeting_2 = greeting
    print(greeting_2("bom dia"))

    print()

    print("hello world")

    print()

    print(greeting_2("boa noite"))

    print()

    hi_ = hi("good morning")
    print(hi_("Davi"))
    print(hi_("Fernando"))
    print(hi_("Artur"))
    print(hi_("Julia"))


    print()


def greeting(message):
    return message

def hi(message):
    def hi_user(name):
        return f"{message},{name}"
    return hi_user

def run(function,*args):
    return function(*args)

if __name__ == "__main__":
     main()
