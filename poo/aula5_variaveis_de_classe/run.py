class MyClass:
    
    static = "Lhama"

    def __init__(self,state) -> None:
        self.__state = state
    
    @classmethod
    def get_static(cls) -> str:
        return cls.static
    
    @classmethod
    def set_static(cls,static : str) -> None | TypeError:

        if static:
            cls.static = static
        else:
            raise TypeError("Value is a invalid")


obj1 = MyClass(True)

print("Obj1=",obj1.get_static())
obj1.static = "hi"

print("Obj1=",obj1.get_static())

MyClass.static = "Hello World"
print("Obj1=",obj1.get_static())

obj2 = MyClass(False)
print(obj2.get_static())

