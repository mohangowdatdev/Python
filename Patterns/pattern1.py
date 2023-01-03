import time

n = int(input("Enter Matrix Size : "))

for i in range(0, n):
    for j in range(0, n):
        print("* ", end=' ')
        time.sleep(0.1)
    time.sleep(0.4)
    print(" ")
