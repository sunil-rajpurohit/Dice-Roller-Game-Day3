import random
import time

def roll_dice():
    print("\n Rolling the dice...")
    time.sleep(1)
    result = random.randint(1,6)
    print(f" You got {result}!\n")



def main_func():
    print("Welcome to the Dice Roller Simulator!\n")
    while True:
        choice = input("Roll the dice?(y/n) :").strip().lower()
        if choice == "y":
            roll_dice()

        elif choice == "n":
            print("\nThanks fpr playing! see you next time! ")
            break
        else:
            print("Invalid Input, Please enter 'y' to roll or 'n' to exit.\n")

if __name__ == "__main__":
    main_func()