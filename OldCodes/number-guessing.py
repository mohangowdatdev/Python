import random
attempts_list = []


def show_score():
    print("---" * 8)
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
    print("---" * 8)



def start_game():
    random_number = int(random.randint(1, 10))
    print("---" * 8)
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? \n")
    wanna_play = input(f"Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No) ")
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError(
                    "Please guess a number within the given range")
            if int(guess) == random_number:
                print("---" * 8)
                print("Nice! You got it! 💡")
                attempts += 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts")
                print("---" * 8)
                play_again = input(
                    "Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower ⬇️")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher ⬆️")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...⚠️")
            print("({})".format(err))
    else:
        print("That's cool, have a good one! 😎")


if __name__ == '__main__':
    start_game()
