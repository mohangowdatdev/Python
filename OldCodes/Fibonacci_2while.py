n = int(input("Enter the nth value: "))
a = 0
b = 1
sum = 0
count=0
print("Fibonacci Series : ", end = " ")
while(sum <= n):
     print(sum, end = " ")
     a = b
     b = sum
     sum = a + b
     count=count+1

print("\n Total terms= ",count)