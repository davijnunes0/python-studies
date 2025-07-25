def main():
    string : str = "Davi"
    method  : str = "upper"

    if hasattr(str,"upper"):
        print("Existe upper()")
        print(getattr(string,method)())
    else:
        print(f"Não existe o método: {method}")

if __name__  == "__main__":
    main()