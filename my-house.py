from colorama import Fore, Back, Style

# Function to draw the ceiling of the house
def ceiling():
    # Top part of the ceiling
    print(Back.LIGHTBLUE_EX + " " * 37 + Back.YELLOW + " " * 6 + Back.LIGHTBLUE_EX + " " * 37 + Style.RESET_ALL)
    # Middle part of the ceiling
    print(Back.LIGHTBLUE_EX + " " * 35 + Back.YELLOW + " " * 10 + Back.LIGHTBLUE_EX + " " * 35 + Style.RESET_ALL)
    # Bottom part of the ceiling
    print(Back.LIGHTBLUE_EX + " " * 30 + Back.YELLOW + " " * 20 + Back.LIGHTBLUE_EX + " " * 30 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 30 + Back.YELLOW + " " * 20 + Back.LIGHTBLUE_EX + " " * 30 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 25 + Back.YELLOW + " " * 30 + Back.LIGHTBLUE_EX + " " * 25 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 25 + Back.YELLOW + " " * 30 + Back.LIGHTBLUE_EX + " " * 25 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 25 + Back.YELLOW + " " * 30 + Back.LIGHTBLUE_EX + " " * 25 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 20 + Back.YELLOW + " " * 40 + Back.LIGHTBLUE_EX + " " * 20 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 20 + Back.YELLOW + " " * 40 + Back.LIGHTBLUE_EX + " " * 20 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 15 + Back.YELLOW + " " * 50 + Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 15 + Back.YELLOW + " " * 50 + Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)

# Function to draw the body of the house
def body():
    i = 1
    while i < 5:
        print(Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 50 + Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)
        i += 1

# Function to draw the window of the house
def window():
    i = 1
    while i < 5:
        print(
            Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 5 + Back.WHITE + " " * 10 + Back.RED + " " * 20 + Back.WHITE + " " * 10 + Back.RED + " " * 5 + Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)
        i += 1

# Function to draw the door of the house
def door():
    i = 1
    while i < 6:
        print(
            Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 9 + Back.LIGHTBLACK_EX + " " * 1 + Back.YELLOW + " " * 10 + Back.RED + " " * 15 +
            Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)
        i += 1

# Function to draw the door handle
def handler():
    i = 0
    while i < 2:
        print(
            Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 8 + Back.LIGHTBLACK_EX + " " * 3 +
            Back.YELLOW + " " * 9 + Back.RED + " " * 15 + Back.LIGHTBLUE_EX + " " * 15 + Style.RESET_ALL)
        i += 1

# Function to draw the grass
def grass():
    i = 1
    while i < 3:
        print(Back.GREEN + " " * 100 + Style.RESET_ALL)
        i += 1

# Function to draw a flower
def flower():
    print(Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 +
          Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 34 + Style.RESET_ALL)
    print(
        Back.GREEN + " " * 18 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 16 + Back.LIGHTCYAN_EX + " " * 2 +
        Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 16 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 +
        Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 32 + Style.RESET_ALL)
    print(Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 +
          Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + Back.GREEN + " " * 34 + Style.RESET_ALL)

# Drawing the elements of the house
ceiling()
body()
window()
body()
door()
handler()
door()
grass()
flower()
grass()
