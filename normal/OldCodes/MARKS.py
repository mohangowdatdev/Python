import time
def calculation():
    sum1 = eng + kan + mat + phy + che + com
    avg1 = sum1 / 6
    sum2 = phy + che + mat
    avg2 =sum2 / 3
    per1 = sum1 / 600 * 100
    per2 = sum2 / 300 * 100
    time.sleep(2)
    print("||Analyzing_the_best_results||")
    time.sleep(2)
    print("Analysing the data")
    time.sleep(0.5)
    print("Calculating the sum")
    time.sleep(0.5)
    print("Calculating the Average")
    time.sleep(0.5)
    print("Calculating the Percentage")
    time.sleep(1)
    print("Fetching the results")
    time.sleep(2)
    print("\n \n \n")
    print("Total Marks Obtained (6 Subjects) = ", sum1, "/600 ")
    print("Total Marks Obtained (PCM) = ", sum2, "/300 ")
    print("Average Marks Obtained (6 Subjects) = ", avg1, "/100")
    print("Average Marks Obtained (PCM) = ", avg2, "/100")
    print("Percentage (6 Subjects) = ",per1,"%")
    print("Percentage (PCM) = ", per2, "%")




print("                                           Welcome to PUC Marks Calculator")
print("                           Enter your Predicted Marks One by one and make sure you are Honest")

rep = input("Do you want to Enter the marks of practicals and theory seperately?? YES OR NO ")
if rep == "yes" or rep == "YES":
    eng = int(input("English: "))
    if eng > 100 or eng < 0:
        eng = 0
        print("*Please enter appropriate value")
    kan = int(input("Kannada: "))
    if kan > 100 or kan < 0:
        kan = 0
        print("*Please enter appropriate value")
    mat = int(input("Maths: "))
    if mat > 100 or mat < 0:
        mat = 0
        print("*Please enter appropriate value")
    phy1 = int(input("Physics  Theory: "))
    if phy1 > 70 or phy1 < 0:
        phy1 = 0
        print("*Please enter appropriate value")
    phy2 = int(input("         Practicals: "))
    if phy2 > 30 or phy2 < 0:
        phy2 = 0
        print("*Please enter appropriate value")
    phy = phy1 + phy2
    che1 = int(input("Chemistry Theory: "))
    if che1 > 70 or che1 < 0:
        che1 = 0
        print("*Please enter appropriate value")
    che2 = int(input("          Practicals: "))
    if che2 > 30 or che2 < 0:
        che2 = 0
        print("*Please enter appropriate value")
    che = che1 + che2
    com1 = int(input("Computer Theory: "))
    if com1 > 70 or com1 < 0:
        com1 = 0
        print("*Please enter appropriate value")
    com2 = int(input("         Practicals: "))
    if com2 > 30 or com2 < 0:
        com2 = 0
        print("*Please enter appropriate value")
    com=com1+com2
else:
    eng = int(input("English: "))
    if eng > 100 or eng < 0:
        eng = 0
        print("*Please enter appropriate value")
    kan = int(input("Kannada: "))
    if kan > 100 or kan < 0:
        kan = 0
        print("*Please enter appropriate value")
    mat = int(input("Maths: "))
    if mat > 100 or mat < 0:
        mat = 0
        print("*Please enter appropriate value")
    phy = int(input("Physics: "))
    if phy > 100 or phy < 0:
        phy = 0
        print("*Please enter appropriate value")
    che = int(input("Chemistry: "))
    if che > 100 or che < 0:
        che = 0
        print("*Please enter appropriate value")
    com = int(input("Computer: "))
    if com > 100 or com < 0:
        com = 0
        print("*Please enter appropriate value")
print()
print()
print()
calculation()















