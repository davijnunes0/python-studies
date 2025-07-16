def main():
    
    
    person_list = []
    get_data(person_list)
    show_persons(person_list)
    
    print("-=" * 90)

    animal = {"name" : "monkey"}

    if animal.get("name"):
        print(animal["name"])

    print("-=" * 90)

def get_data(person_list: dict):

    name = str(input("What's your name: "))

    try:
        age = int(input("How old are you: "))
        heigth = float(input("Heigth: "))
    except ValueError as e:
         print(e)

    person_list.append(signup_person(name,age,heigth))


def signup_person(name : str, age : int,heigth : float) -> dict:
    
    person = {"name":name,"age":age,"heigth":heigth}
    return person


def show_persons(person_list: dict):

    for person in person_list:
        print(person["name"],person["age"],person["heigth"])


if __name__ == "__main__":
    main()
