import math

a = float(input("Side 1 - "))
b = float(input("Side 2 - "))
c = float(input("Side 3 - "))

s = (a+b+c)/2

area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))

print("Area of given triangle is ", area)
