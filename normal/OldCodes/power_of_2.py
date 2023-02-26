n=int(input("Enter the Number: "))
m=n
status=0
while m>2:
    if m%2==0:
        status=1
        break
    else:
        m=m/2
if status:
    print(n," is a power of 2")
else:
    print(n," is not a power of 2")