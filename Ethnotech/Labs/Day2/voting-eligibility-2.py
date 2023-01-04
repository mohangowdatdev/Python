class Persona:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

    def talk(self):
        print("Hi I'm ", self.name, "and my age is ", self.age)

    def vote(self):
        if self.age < 18:
            print("Not Eligible try again after", 18 - self.age, "years")
        else:
            print("Eligible. Congratulations !!")


num = int(input("How many members ? - "))

for i in range(0, num):
    print(i)
p1 = Persona("Mohan", "Male", 21)
p1.talk()
p1.vote()
p2 = Persona("Balaji", "Male", 17)
p2.talk()
p2.vote()
