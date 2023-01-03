class Person:
    def __init__(self):
        self.name = "Mohan"
        self.gender = "M"
        self.age = 1

    def inp(self):
        self.age = int(input("Enter Age - "))

    def talk(self):
        print("Hi I'm ", self.name, "and my age is ", self.age)

    def vote(self):
        if self.age < 18:
            print("Not Eligible try again after", 18 - self.age, "years")
        else:
            print("Eligible. Congratulations !!")


p1 = Person()
p1.inp()
p1.talk()
p1.vote()
