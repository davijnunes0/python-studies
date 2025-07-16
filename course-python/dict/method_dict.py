from copy import deepcopy

def main():
    
    person = {
    "name" : "Julia",
    "age" : 20}

    print(len(person))

    print()

    for data in person.keys():
        print(data)

    print()

    for data in person.values():
        print(data)

    print()

    for data in person.items():
        print(data)

    print()

    if person.get("name"):
        print(person)

    print()
    
    person.setdefault("heigth",1.90)
    

        person.update({"salary": 2000.00},pet="dog")


    print(person)
    

    dict1 = {
        "c1" : [1,2,3] 
        }

    # Deepcopy
    dict3 = deepcopy(dict1)

    # Shallow copy    
    dict2 = dict1.copy()

    print(dict1,dict2)
    print("-=" * 100)
    
    dict1["c1"].append(4)
    dict2["c1"].append(5)

    print(dict1,dict2)

    print("-=" * 100)
    print(dict1,dict2,dict3)
    


if __name__ == "__main__":
    main()
