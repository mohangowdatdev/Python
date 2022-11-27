""" Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
   Score Grade
   >= 9.0 A
   >= 8.0 B
   >= 7.0 C
   >= 6.0 D
   < 6.0 F
   If the user enters a value out of range, print a suitable error message and exit.
 """


score = float(input("Enter Score: "))

if score > 10.0:
    print("Out of Range!")
    exit() 
elif score < 0.0:
    print("Out of Range!")
    exit()

if score >= 9.0:
    print("A")
elif score >= 8.0:
    print("B")
elif score >= 7.0:
    print("C")
elif score >= 6.0:
    print("D")
else:
    print("F")
