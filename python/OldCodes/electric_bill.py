olr=int(input("Enter the Old readings, Old read=  "))
nr=int(input("Enter the New readings, New read=  "))

u=int(nr-olr)
print("Units consumed, units= ",u)

if u<30:
    amt=u*3.5
else:
    if u<50:
        amt=(29*3.5)+(u-29)*4.25
    else:
        if u<100:
            amt=(29*3.25)+(20*4.25)+(u-49)*5.25
        else:
            amt = (29 * 3.25) + (20 * 4.25) + (50*5.25) + (u-99)*5.85

print("The bill for consumption of ", u ," units is $",amt)


