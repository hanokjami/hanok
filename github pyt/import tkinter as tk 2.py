import time
import random

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a mysterious land. Your goal is to reach the treasure at the end.")
    print("Be careful! Your choices will determine your fate.")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest():
    print("You enter a dark forest.")
    time.sleep(1)
    print("You hear strange sounds all around you.")
    time.sleep(1)

    choices = ["Continue deeper into the forest", "Turn back"]
    choice = make_choice(choices)

    if choice == 1:
        print("You encounter a mystical creature.")
        time.sleep(1)
        print("It offers you a magical amulet.")
        time.sleep(1)

        choices = ["Accept the amulet", "Decline the amulet"]
        choice = make_choice(choices)

        if choice == 1:
            print("The amulet glows, granting you protection.")
        else:
            print("The creature disappears, and you continue your journey without the amulet.")

        print("You exit the forest.")
        return True
    else:
        print("You decide to turn back and leave the forest.")
        return False

def mountain():
    print("You reach a tall mountain.")
    time.sleep(1)
    print("You see a treacherous path going up.")
    time.sleep(1)

    choices = ["Climb the mountain", "Look for another way"]
    choice = make_choice(choices)

    if choice == 1:
        print("You start climbing the mountain.")
        time.sleep(2)

        if random.choice([True, False]):
            print("You successfully reach the top of the mountain.")
            return True
        else:
            print("You slip and fall. Ouch!")
            return False
    else:
        print("You search for another way around the mountain.")
        return True

def treasure():
    print("You finally reach the treasure!")
    time.sleep(1)
    print("Congratulations, you have completed the adventure!")

def main():
    introduction()

    if forest():
        if mountain():
            treasure()
        else:
            print("Your journey ends here.")

if _name_ == "_main_":
    main()