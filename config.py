# Screen configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Slot Machine"
SCREEN_BG_COLOR = "black"

# Game controls
KEY_TO_PULL = "space"
KEY_TO_EXIT = "Escape"

# Machine configuration
NUMBER_OF_SLOTS = 3
DEFAULT_SLOT_SIZE = 20  # Do not change this value, it is Turtle default size
SLOT_SHAPE = "square"
VERTICAL_SHAPE_STRETCH = 5
HORIZONTAL_SHAPE_STRETCH = 5
OUTLINE_SIZE = 10
STARTING_Y_POSITION = 0

# Slot types
TOP_SECONDARY_SLOT = "top"
BOTTOM_SECONDARY_SLOT = "bottom"

# Slot colors
MAIN_SLOT_COLOR = "white"
SECONDARY_SLOT_COLOR = "gray"
MAIN_SLOT_OUTLINE_COLOR = "black"
SECONDARY_SLOT_OUTLINE_COLOR = "black"
MAIN_SLOT_NUMBER_COLOR = "red"
SECONDARY_SLOT_NUMBER_COLOR = "orange"

# Game logic
MIN_PULL_CYCLES = 10
MAX_PULL_CYCLES = 20

# Slot configuration
SLOT_ALIGNMENT = "center"
SLOT_FONT_SIZE = 50
SLOT_FONT = ("Courier", SLOT_FONT_SIZE, "bold")

# Money configuration
MONEY_ALIGNMENT = "center"
MONEY_FONT = ("Courier", 20, "bold")
DEFAULT_MONEY_COLOR = "white"
LOW_MONEY_COLOR = "red"
MONEY_X_POSITION = 0
MONEY_Y_POSITION = 360
DEFAULT_MONEY = 1000
WIN_PRIZE = 2000
PULL_COST = 50

# Instructions configuration
INSTRUCTIONS_ALIGNMENT = "center"
INSTRUCTIONS_FONT = ("Arial", 30, "bold")
INSTRUCTIONS_COLOR = "white"
INSTRUCTIONS_X_POSITION = 0
INSTRUCTIONS_Y_POSITION = -300
DEFAULT_INSTRUCTIONS = "Press SPACE to pull!\n"
HOW_TO_EXIT = "Press Escape to exit the game."
HOW_TO_EXIT_FONT = ("Arial", 14, "normal")

# Messages configuration
MESSAGES_ALIGNMENT = "center"
MESSAGES_FONT = ("Arial", 25, "bold")
MESSAGES_COLOR = "white"
MESSAGES_X_POSITION = 0
MESSAGES_Y_POSITION = 280
