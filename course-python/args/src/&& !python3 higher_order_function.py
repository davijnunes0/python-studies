def main():
    
    greeting_2 = greeting
    print(greeting_2("bom dia"))
    print("hello world")

def greeting(message):
    return message

def run(function,*args):
    return function(args)

if __name__ == "__main__":
     main()
