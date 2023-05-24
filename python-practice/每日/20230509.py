class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view(self):
        print(self.name, self.age)


s = Student('fme', 32)
s.view()
