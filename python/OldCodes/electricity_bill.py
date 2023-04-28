amt=int(input("Enter the Total amount of the purchase, Amount= "))

if amt>1000:
    dis=8
else:
    dis=0
dis=int(dis/100*amt)
fa=int(amt-dis)

print("Final amount is ",fa)
print("Discount Applied is ",dis)