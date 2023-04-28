import time
import random

print("|| Welcome to the game ||")
guide = input("Do you want a quick Introduction ?? type 'yes' or 'no' \n")
if guide == "yes":
    print("----"*6)
    print("Here's a Quick Guide 📰")
    print("-" * 6)
    print("> The game is simple")
    print("> I will guess a number, and you will have to predict it in 10 moves and 90 seconds.")
    print("> I will be providing you hint in every prediction you make wrong.")
    print("> I will say 'ALMOST CORRECT' if +- 3")
    print(">            'BIT NEAR' if +- 10")
    print(">            'TOO FAR' if none of the above are correct.")
    print("----" * 6)
    time.sleep(15)

print("👁 Alright!! Let's begin the game. Now close your eyes for 3 seconds!! 👁")

time.sleep(5)

rn = random.randint(0, 50)
print("----" * 6)
print(f"The Random number I picked was : 💡 >>[ {rn} ]<< 💡:) ")
print("----" * 6)


for i in range(30):
    time.sleep(0.05)
    print("*"*i , "⬆️")
print("\n")
print("----" * 6)

print("Now try to predict a number. Good luck. Your time begins now !! 💪")
start=time.time()

i=0
while True:
    i=i+1
    gn = int(input("Enter your predicted number: "))
    if (rn - gn) <= 3 and (rn - gn) >= 1:
        print("ALMOST CORRECT")
    elif (rn - gn) <= 10 and (rn - gn) >= 3:
        print("BIT NEAR")
    elif (rn - gn) >= -3 and (rn - gn) <= -1:
        print("ALMOST CORRECT")
    elif (rn - gn) >= -10 and (rn - gn) <= -3:
        print("BIT NEAR")
    elif rn == gn:
        print("|You are perfect. You can scroll to the top and check the number|")
        break
    else:
        print("||TOO FAR||")
    if i>10:
        print("Sorry You are out of moves, TRY AGAIN")
        print("Your number was ")
        print(rn)
        break

    if gn > 50 or gn < 0:
        print("Please Enter a number only between 0 and 50")

print("----" * 6)
print()
print()
end= time.time()
tt=int(end-start)
if tt > 90:
    print("We are sorry, You ran out of time. You only had 90 seconds.")
if i<=10 and tt<=90:
    print("Congratulations, You have identified the correct element "+ str(gn) +" in")
    print(str(i) + " counts")
    print("and")
    print(str(tt)+" seconds")



