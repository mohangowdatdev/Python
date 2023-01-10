td=int(input("Enter the number of days, days= "))

y=td/365
td=td%365
m=td/30
d=td%30
y=int(y)
m=int(m)
d=int(d)

print("Total number of Days are, Days= ",d)
print("Total number of Months are, Month= ",m)
print("Total number of Years are, Year= ",y)


