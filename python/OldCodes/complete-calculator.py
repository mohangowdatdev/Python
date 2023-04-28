print("Complex Calci")
print("____________")
print()


def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def subtraction():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 0
    while n != 0:
        ans = ans - n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def average():
    # an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]


# main...
while True:
    listy = []
    print()
    print(" Simple Calculator in python by Mohan Gowda T :}")
    print("_______________________")
    print(" Enter 'a' for addition")
    print(" Enter 's' for Subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print("_______________________")
    print(" Enter 'q' for quit")
    print("_______________________")
    c = input(" >> ")
    if c != 'q':
        if c == 'a':
            listy = addition()
            print("Ans = ", listy[0], " total inputs ", listy[1])
        elif c == 's':
            listy = subtraction()
            print("Ans = ", listy[0], " total inputs ", listy[1])
        elif c == 'm':
            listy = multiplication()
            print("Ans = ", listy[0], " total inputs ", listy[1])
        elif c == 'v':
            listy = average()
            print("Ans = ", listy[0], " total inputs ", listy[1])
        else:
            print("Sorry, invalid character")
    else:
        break
