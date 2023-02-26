l=int(input("Enter the nth value: "))
f=0
s=1
t=0
count=0
print("Fibonacci Series : ", end=" ")
for i in range(l):
    if t<=l:
        pass
    else:
        break
    print(t,end=" ")
    f=s
    s=t
    t=f+s
    count=count+1
print("\n Total terms= ",count)