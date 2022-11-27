a=int(input("Enter the First number, a= "))
b=int(input("Enter the second number, b= "))

print("+  1st Method- With using third variable")
c=a
a=b
b=c
print("The interchanged variables are a = ",a," b = ",b)
print("+  2nd Method- Without using third variable")
a,b=b,a
a=a+b
b=a-b
a=a-b
print("The interchanged variables are a = ",a," b = ",b)
print("+  3rd Method- Simultaneous interchanging *only for python ")
a,b=b,a
a,b=b,a
print("The interchanged variables are a = ",a," b = ",b)


