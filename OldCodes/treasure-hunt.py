import time

print('''------------------------------------------------------------------
 _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
        
------------------------------------------------------------------''')

# python program for treasure island
print("==========================================================")
print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("==========================================================")

print("💡 Please input reply in lowercase!!")
rep = 'y'
while True:
    print("-----------------------------------------------------------------------------------------")
    inp1 = input("You gave an entrance into a dark forest and come into a dilemma to go 'left' or 'right'. Where do "
                 "you wanna go, 'left' or 'right' ?? - ")
    if inp1 != "left":
        print("You fell into a hole. Game Over Try again!!")
        time.sleep(2)
        continue
    else:
        inp2 = input("You move left and see ahead that there is large river. You can either swim to the other side or "
                     "wait for the boat to arrive. Will you 'wait' or 'swim' ?? - ")
        if inp2 != "wait":
            print("You made up your mind to swim to the other side. Unfortunately a crocodile attacked you. Game over "
                  "Try again!!")
            time.sleep(2)
            continue
        else:
            inp3 = input("You crossed the river using the boat. You find a glowing shelter far away and decide to walk "
                         "there. When you reach there you saw 3 doors painted with 'red' 'yellow' and 'blue'. Which "
                         "door you wanna open ? - ")
            if inp3 == "blue":
                print("You got eaten by beasts. Game over try again!!")
                time.sleep(2)
                continue
            elif inp3 == "yellow":
                print("Congratulations!! You have found your treasure. Have a Rocking Time :)")
                exit()
            elif inp3 == "red":
                print("You entered the room full of fire and got burned. Game over try again!!")
                time.sleep(2)
                continue
            else:
                print("Invalid door!! Try again")
                time.sleep(2)
                continue
