import random

lst=[1,2,3,4,5,6]

print("\n Welcome to DICE Roller \n")
print("-----------------------------------------------------------------------------------")

while True:
    num= random.choice(lst)
    print("Number: ", num)
    ans=input()
    if ans == 'n' or ans == 'N':
        break
    print("------------------------------------------------------------------------------------")
