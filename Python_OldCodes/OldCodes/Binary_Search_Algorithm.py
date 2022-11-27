from array import *
a= array('i',[])
n=int(input("Size = "))

for i in range(n):
    b = int(input("Values = "))
    a.append(b)

print(a)

s = int(input("Enter the search element: "))
for z in a:
    if z == s:
        print("Element Found at position ",a.index(z)+1)
        break
else:
    print("Element not found")
