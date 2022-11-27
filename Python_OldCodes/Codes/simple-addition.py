import time
print("Welcome to Python Calculator - Simple Addition")
print("----------------------------------------------")

print("How many numbers do you want to add ? (max 5)")
a = int(input())

time.sleep(1)

if a > 5:
    print("Idiot I said enter below 5 numbers :}")
if a == 0:
    print("Stop Kidding with me please :{")
if a == 1:
    print("Are you out of your mind how can you add 1 digit !!")
if a == 2:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    print(n1 + n2)

if a == 3:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = int(input("Third Number: "))
    print(n1 + n2 + n3)

if a == 4:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = int(input("Third Number: "))
    n4 = int(input("Fourth Number: "))
    print(n1 + n2 + n3 + n4)

if a == 5:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = int(input("Third Number: "))
    n4 = int(input("Fourth Number: "))
    n5 = int(input("Fifth Number: "))
    print(n1 + n2 + n3 + n4 + n5)
