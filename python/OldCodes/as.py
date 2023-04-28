import os
import time


def progress_bar(seconds):
    for progress in range(0, seconds + 1):
        percent = (progress * 100) // seconds
        print("\n")
        print("Loading...")
        print("<" + ("=" * progress) + (" " * (seconds - progress)) + "> " + str(percent) + "%")
        print("\n")
        time.sleep(1)
        os.system('clear')

    # Main Program Starts Here....


progress_bar(10)
username = input("Type your username:")
