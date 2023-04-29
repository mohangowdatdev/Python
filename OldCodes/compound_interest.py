pa=int(input("Enter the amount taken: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time taken: "))
na=pa
y=1
while y<=t:
    na=na*(1+r/100)
    y+=1

ci=na-pa
print("The compound interest is ",ci)
print("Net amount= ",na)