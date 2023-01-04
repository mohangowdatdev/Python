class Maths:
    def mm(self):
        m = float(input("Enter Maths Marks: "))
        # print(f"Math = {m}")
        return m


class Science:
    def sm(self):
        s = float(input("Enter Science Marks: "))
        # print(f"Science = {s}")
        return s


class Name:
    def nm(self):
        name = input("Enter Name : ")
        return name


class Student(Maths, Science):
    sc = Science()
    ma = Maths()
    ne = Name()
    na = ne.nm()
    m = ma.mm()
    s = sc.sm()

    def stud(self):
        print(f"Name : {self.na}")
        print(f"Math = {self.m}")
        print(f"Science = {self.s}")


s1 = Student()
s1.stud()
