
import time
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
reply = 'y'
c = 0
u = 0
d = 0
while reply == 'y':
    print("-------------------------------------------------------------------------")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. - "))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number!! It's a draw")
        d += 1
        continue
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number!! It's a draw")
        d += 1
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
        u += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        c += 1
    elif computer_choice > user_choice:
        print("You lose")
        c += 1
    elif user_choice > computer_choice:
        print("You win!")
        u += 1
    elif computer_choice == user_choice:
        print("It's a draw")
        d += 1
    reply = input("Play again ? (y/n) - ")

match = u+d+c
print("=========================================================================")
print("💡 Wait while the report is being generated: ")
print("-------------------------------------------------------------------------")
time.sleep(2)
print(f"You win {u} times | Computer win {c} times | Draw for {d} times")
print(f"Total number of matches is {match}")
per = u / match * 100
print(f"Your win percentage is {per}%. Well done!!")