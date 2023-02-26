av=20
i=1
x=int(input("Hello Kid how many candies do you want? -  "))
while i<=x:
    if(i>av):
        print("Sorry we have only", av , "Candies")
        break
    else:
        print("candy", i)
    i+=1
