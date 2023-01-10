a=int(input("Enter the First number, a= "))
b=int(input("Enter the second number, b= "))
c=int(input("Enter the third number, c= "))

large=a
if b>large:
    large=b
if c>large:
    large=c

small=a
if b<small:
    small=b
if c<small:
    small=c

secl=(a+b+c)-(large+small)

print("Largest number is ",large)
print("Smallest number is ",small)
print("second largest number is ",secl)