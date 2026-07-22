# BATTLESHIP GAME by Arda Ertuğ Sevindik

import random          # Used 3 import modules
import os
import time

def clear_screen():
    print("\033[2J\033[H", end="")               # Function to clear the screen

# Code written for the opening sequence of the game
opening_text = """
     .....WELCOME TO BATTLESHIP GAME!.....
     .....................................
     .....................................
     Created by Arda Ertuğ Sevindik.......
     .....................................
     ......Press Enter key to start.......
"""

screen_display = ""

for char in opening_text:                          # Code to print the opening text letter by letter
    clear_screen()                                 # Clears screen each time and appends a character
    screen_display = screen_display + char
    print(screen_display)
    time.sleep(0.03)

time.sleep(0.5)

for i in range(7):    # Flashing text effect section
    clear_screen()   # Clears the screen, prints empty space, then re-prints text
    print("")
    time.sleep(0.3)
    clear_screen()
    print(opening_text)
    time.sleep(0.3)
    print("")
input() # Waits for Enter key press to proceed to the loading screen

loading_bar_length = 30       # Loading bar length configuration
fill_speed = 0.1

for i in range(loading_bar_length + 1):
    clear_screen()

    filled = "█" * i
    empty = "-" * (loading_bar_length - i)

    print("\n" * 5)    # Prints empty lines for spacing
    print(f"      LOADING GAME... %{int((i / loading_bar_length) * 100)}")  # Calculates and displays progress percentage
    print(f"      [{filled}{empty}]")  # Progress bar display

    time.sleep(fill_speed)

print("\n          LOADING COMPLETE!    ")
time.sleep(1)

clear_screen()

for i in range(7):        # Warning loop informing the user about having 3 guesses
    print()
    print("YOU HAVE 3 GUESSES, BE CAREFUL!")
    time.sleep(0.25)
    clear_screen()
    print("")
    clear_screen()
    time.sleep(0.25)

def display_map(grid_list):              # Code for displaying the sea grid
    print("SEA STATUS:")
    for cell in grid_list:
        print("[", cell, "]", end=" ")
    print()
    print()


def start_game():        # Main game logic
    while True:            # Loop to allow replaying
        print("--- NEW GAME ---")

        ship_location = random.randint(1, 5)  # Randomly selects a ship position between 1 and 5 (inclusive)
        sea = [1, 2, 3, 4, 5]
        won = False

        for attempt in range(1, 4):    # Loop for 3 attempts. Exits when attempts are exhausted
            display_map(sea)
            message = "Attempt " + str(attempt) + " - Select a target to fire (1-5): "
            guess = int(input(message))
            time.sleep(0.25)
            print("Firing...")
            time.sleep(1.5)
            clear_screen()

            if guess < 1 or guess > 5:   # Input validation warning
                print("WARNING: Please enter a number between 1 and 5 only!")
                continue

            match guess:
                case _ if guess == ship_location:
                    for hit_step in range(7):   # Flashing text loop when ship is hit
                       print()
                       print("...YOU HIT THE SHIP! CONGRATULATIONS! ...") # Hit message
                       time.sleep(0.25)
                       clear_screen()
                       print("")
                       clear_screen()
                       time.sleep(0.25)
                    print("...YOU HIT THE SHIP! CONGRATULATIONS! ...")
                    won = True

                    sea[guess - 1] = "SHIP"
                    display_map(sea)
                    time.sleep(4)
                    break    # Exit loop

                case _:
                    print()
                    print("Missed...")   # Miss message
                    time.sleep(2)
                    clear_screen()
                    sea[guess - 1] = "X"
        if not won:
            print("You lost! The ship was at position:", ship_location)

        while True:     # Replay prompt loop
            continue_choice = input("Do you want to continue? (Y/N): ").upper()
            if continue_choice == 'Y' or continue_choice == 'N':
                break
            else:
                print("Please enter Y or N!")
        if continue_choice == 'N':
            time.sleep(0.5)
            clear_screen()
            print(".....Thanks for playing the game!....")
            time.sleep(1)
            print("..........................................")
            time.sleep(0.2)
            print("..........................................")
            time.sleep(0.2)
            print("..........................................")
            input(".......Press Enter key to exit.......")
            break
        if continue_choice == 'Y':
            clear_screen()
            time.sleep(0.5)
            print(".......Game Restarting, Get Ready.....")
            time.sleep(1)
            print("...................3......................")
            time.sleep(1)
            print("...................2......................")
            time.sleep(1)
            print("...................1......................")
            time.sleep(1)
            clear_screen()

start_game()