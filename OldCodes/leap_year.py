year=int(input("Enter the Year, Year= "))

if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
