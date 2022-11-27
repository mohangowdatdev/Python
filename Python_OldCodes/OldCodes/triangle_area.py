import math
a=int(input("Enter the First side, a= "))
b=int(input("Enter the second side, b= "))
c=int(input("Enter the third side, c= "))

s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
ar=int(ar)

print("Area of circle is ",ar)