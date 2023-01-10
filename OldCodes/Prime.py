n=int(input("Enter the number to be checked: n= "))

for i in range(2,n):
    if n%i==0:
        print("not Prime Number")
        break
else:
    print("Prime Number")