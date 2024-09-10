from colorama import Back, Style

# Helper function to draw repeated patterns
def draw_rectangle(width, height, color):
    for _ in range(height):
        print(color + " " * width + Style.RESET_ALL)

# Function to draw the ceiling with specified width and reduction in yellow pattern
def draw_ceiling():
    for i in range(5):
        side_space = 40 - i * 5  # gradually reduces the side space
        yellow_width = 10 + i * 10  # gradually increases yellow pattern
        print(Back.LIGHTBLUE_EX + " " * side_space + Back.YELLOW + " " * yellow_width + " " * side_space + Style.RESET_ALL)

# Function to draw the main body of the house
def draw_body():
    draw_rectangle(80, 4, Back.LIGHTBLUE_EX + " " * 15 + Back.RED)

# Function to draw the window section with reusable window pattern
def draw_window():
    window_pattern = (
        Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 5 + Back.WHITE + " " * 10 +
        Back.RED + " " * 20 + Back.WHITE + " " * 10 + Back.RED + " " * 5 + " " * 15 + Style.RESET_ALL
    )
    draw_rectangle(80, 4, window_pattern)

# Function to draw the door
def draw_door():
    door_pattern = (
        Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 9 +
        Back.LIGHTBLACK_EX + " " * 1 + Back.YELLOW + " " * 10 + Back.RED + " " * 15 + " " * 15 + Style.RESET_ALL
    )
    draw_rectangle(80, 5, door_pattern)

# Function to draw the door handle
def draw_door_handle():
    handle_pattern = (
        Back.LIGHTBLUE_EX + " " * 15 + Back.RED + " " * 15 + Back.YELLOW + " " * 8 +
        Back.LIGHTBLACK_EX + " " * 3 + Back.YELLOW + " " * 9 + Back.RED + " " * 15 + " " * 15 + Style.RESET_ALL
    )
    draw_rectangle(80, 2, handle_pattern)

# Function to draw the grass area
def draw_grass():
    draw_rectangle(100, 5, Back.GREEN)

# Function to draw flowers in the grass
def draw_flower():
    print(Back.GREEN + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 20 + Back.LIGHTCYAN_EX + " " * 2 + " " * 34 + Style.RESET_ALL)
    print(Back.GREEN + " " * 18 + Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 16 +
          Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 16 +
          Back.LIGHTCYAN_EX + " " * 2 + Back.YELLOW + " " * 2 + Back.LIGHTCYAN_EX + " " * 2 + " " * 32 + Style.RESET_ALL)
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
