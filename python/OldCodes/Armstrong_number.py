n=int(input("Enter the number: "))
m=int(n)
sum=0
while m>0:
    rem=m%10
    sum=sum+(rem**3)
    m//=10
if int(sum)==int(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
