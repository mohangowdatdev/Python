class Person:

    def __init__(self):
        self.age = None

    def inp(self):
        self.age = int(input("Enter Age - "))


p1 = Person()
p1.inp()
print("Age = ", p1.age, "years")
