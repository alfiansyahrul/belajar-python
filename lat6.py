class MyClass:
    nama = "Babastudio"

p1 = MyClass()
print(p1.nama)

class Person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age =age

    def myfunc(abc):
        print("Hello My Name is " + abc.name)
        print("My Age is " + str(abc.age))

p1 = Person("Syahrul", 26)
p1.myfunc()