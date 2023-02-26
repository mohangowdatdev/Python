n=int(input("Enter the number: "))
m=n
sum=0
while n!=0:
    rem=n%10
    sum=sum+rem
    n=n/10
sum=int(sum)
print("The sum of digits in the number ",m," is ",sum)