from colorama import Back, Style

def draw_rectangle(width, height, color):
    for _ in range(height):
        print(color + " " * width + Style.RESET_ALL)

def draw_ceiling():
    print(Back.LIGHTBLUE_EX + " " * 37 + Back.YELLOW + " " * 6 + " " * 37 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 35 + Back.YELLOW + " " * 10 + " " * 35 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 30 + Back.YELLOW + " " * 20 + " " * 30 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 25 + Back.YELLOW + " " * 30 + " " * 25 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 20 + Back.YELLOW + " " * 40 + " " * 20 + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + " " * 15 + Back.YELLOW + " " * 50 + " " * 15 + Style.RESET_ALL)

def draw_body():
    draw_rectangle(80, 4, Back.LIGHTBLUE_EX + " " * 15 + Back.RED)

def draw_window():
    for _ in range(4):
        print(Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 5 + Back.WHITE + " " * 10 + Back.RED + " " * 20 + Back.WHITE + " " * 10 + Back.RED + " " * 5 + " " * 15 + Style.RESET_ALL)

def draw_door():
    for _ in range(5):
        print(Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 9 + Back.LIGHTBLACK_EX + " " * 1 + Back.YELLOW + " " * 10 + Back.RED + " " * 15 + " " * 15 + Style.RESET_ALL)

def draw_door_handle():
    for _ in range(2):
        print(Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 8 + Back.LIGHTBLACK_EX + " " * 3 + Back.YELLOW + " " * 9 + Back.RED + " " * 15 + " " * 15 + Style.RESET_ALL)

def draw_grass():
    for _ in range(5):
        print(Back.GREEN + " " * 100 + Style.RESET_ALL)

def draw_flower():
    print(Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 34 + Style.RESET_ALL)
    print(Back.GREEN + " " * 18 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 16 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 16 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 32 + Style.RESET_ALL)
    print(Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 34 + Style.RESET_ALL)

# Drawing the house
draw_ceiling()
draw_body()
draw_window()
draw_body()
draw_door()
draw_door_handle()
draw_door()
draw_grass()
draw_flower()
draw_grass()
