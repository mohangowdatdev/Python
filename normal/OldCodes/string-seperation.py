import time
str = input("Enter the string: ")
print(" ")
c = 0
time.sleep(2)
print("Method 1")
print("------------------------")
while c < len(str):
    letter = str[c]
    print(c, " ", letter)
    c += 1
# -----------------------------------------------------------------------------------
print("")
time.sleep(2)
print("Method 2")
print("------------------------")
for letter in str:
    print(letter)
