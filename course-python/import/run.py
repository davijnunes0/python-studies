import run_module
from hello.hello_user  import speaky_hello

def main():
    print("Hello in module run")
    print("Name module:", __name__)
    
    print("-=" * 100)
    speaky_hello()

if __name__ == "__main__":
    main()
