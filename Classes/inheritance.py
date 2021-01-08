

class Base1:
    def __init__(self):
        self.a = "base1"


class Base2:
    def __init__(self):
        self.b = "base2"


class Base3:
    def __init__(self):
        self.c = "base3"

    def double_base_string(self) -> str:
        return self.c * 2


class DerivedClass1(Base1):
    def __init__(self):
        super().__init__()
        self.__a1 = "base1_private"
        # super().__init__()    =   Base1.__init__(self)
        #
        # super() is equivalent to "super(DerivedClass1, self)"
        #
        self.d = "DerivedClass1"


obj1 = DerivedClass1()
print(obj1.a)
print(obj1.d)
print("dir(obj1)")
print(dir(obj1))
# print(obj1.__a1)
print(obj1._DerivedClass1__a1)
print(super)
print(dir(super))
# print(super())    ->  RuntimeError: super(): no arguments
print("--------------------------------------------------------------------------------------")
print(dir())
print("--------------------------------------------------------------------------------------")
print(dir(__builtins__))
print("--------------------------------------------------------------------------------------")


if isinstance(obj1, DerivedClass1):
    print("obj1 is instance of DerivedClass1 or is object of class derived from DerivedClass1")

if isinstance(obj1, Base1):
    print("obj1 is instance of Base1 or is object of class derived from Base1")

if issubclass(DerivedClass1, Base1):
    print("DerivedClass1 is class derived from Base1")

if issubclass(DerivedClass1, Base2):
    print("DerivedClass1 is class derived from Base2")
else:
    print("DerivedClass1 is NOT class derived from Base2")

#
#
#
# 9.7. Odds and Ends


class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print("--------------------------------------------------------------------------------------")
print(john.name)
print(john.dept)
print(john.salary)
print("--------------------------------------------------------------------------------------")
