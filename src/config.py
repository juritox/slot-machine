"""
Configuration file for the Slot Machine game.

This module contains all the constant values used throughout the game,
including screen settings, game controls, machine configuration,
slot settings, and display parameters.
"""

# Screen configuration
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Slot Machine"
SCREEN_BG_COLOR: str = "black"

# Game controls
KEY_TO_PULL: str = "space"
KEY_TO_EXIT: str = "Escape"

# Machine configuration
NUMBER_OF_SLOTS: int = 3  # Number of slots must be at least 2
DEFAULT_SLOT_SIZE: int = 20  # Do not change this value, it is Turtle default size
SLOT_SHAPE: str = "square"
VERTICAL_SHAPE_STRETCH: int = 5
HORIZONTAL_SHAPE_STRETCH: int = 5
OUTLINE_SIZE: int = 10
STARTING_Y_POSITION: int = 0

# Slot types
TOP_SECONDARY_SLOT: str = "top"
BOTTOM_SECONDARY_SLOT: str = "bottom"

# Slot colors
MAIN_SLOT_COLOR: str = "white"
SECONDARY_SLOT_COLOR: str = "gray"
MAIN_SLOT_OUTLINE_COLOR: str = "black"
SECONDARY_SLOT_OUTLINE_COLOR: str = "black"
MAIN_SLOT_DISPLAY_COLOR: str = "red"
SECONDARY_SLOT_DISPLAY_COLOR: str = "orange"

# Slot values
# Avoid using symbols like 7️⃣ which combines more Unicode characters
SLOT_SYMBOLS: tuple[str, ...] = ("🍒", "🍋", "🍊", "🍇", "🔔", "💎", "🎰")
SLOT_NUMBERS: tuple[int, ...] = tuple(range(1, 10))  # 1 to 9
USE_SYMBOLS: bool = True  # Set as False to use numbers

# Jackpot configuration
JACKPOT_ENABLED: bool = True  # Set as False to disable jackpot
JACKPOT_WINNING_SYMBOL: str = "🎰"  # Must be included in SLOT_SYMBOLS list
JACKPOT_WINNING_NUMBER: int = 7  # Must be included in SLOT_NUMBERS list
JACKPOT_PRIZE_MULTIPLIER: int = 17
JACKPOT_COLOR: str = "orange"
JACKPOT_X_POSITION: int = 380
JACKPOT_Y_POSITION: int = -360

# Game logic
MIN_PULL_CYCLES: int = 10  # Must be at least 1 and not greater than MAX_PULL_CYCLES
MAX_PULL_CYCLES: int = 20  # Must not be greater than 100

# Slot configuration
SLOT_ALIGNMENT: str = "center"
SLOT_FONT_SIZE: int = 50
SLOT_FONT: tuple[str, int, str] = ("Courier", SLOT_FONT_SIZE, "bold")

# Money configuration
MONEY_ALIGNMENT: str = "center"
MONEY_FONT: tuple[str, int, str] = ("Courier", 20, "bold")
DEFAULT_MONEY_COLOR: str = "white"
LOW_MONEY_COLOR: str = "red"
MONEY_X_POSITION: int = 0
MONEY_Y_POSITION: int = 360
DEFAULT_MONEY: int = 1000
WIN_PRIZE: int = 700  # must be at least twice as big as PULL_COST
PULL_COST: int = 50

# Instructions configuration
INSTRUCTIONS_ALIGNMENT: str = "center"
INSTRUCTIONS_FONT: tuple[str, int, str] = ("Arial", 30, "bold")
INSTRUCTIONS_COLOR: str = "white"
INSTRUCTIONS_X_POSITION: int = 0
INSTRUCTIONS_Y_POSITION: int = -300
DEFAULT_INSTRUCTIONS: str = "Press SPACE to pull!\n"
HOW_TO_EXIT: str = "Press Escape to exit the game."
HOW_TO_EXIT_FONT: tuple[str, int, str] = ("Arial", 14, "normal")

# Messages configuration
MAIN_MESSAGES_ALIGNMENT: str = "center"
MAIN_MESSAGES_FONT: tuple[str, int, str] = ("Arial", 25, "bold")
MESSAGES_COLOR: str = "white"
MAIN_MESSAGES_X_POSITION: int = 0
MAIN_MESSAGES_Y_POSITION: int = 280
MONEY_MESSAGES_FONT: tuple[str, int, str] = ("Arial", 14, "normal")
PRIZE_MESSAGES_ALIGNMENT: str = "right"
PRIZE_MESSAGES_X_POSITION: int = 380
PRIZE_MESSAGES_Y_POSITION: int = 370
PULL_MESSAGES_ALIGNMENT: str = "left"
PULL_MESSAGES_X_POSITION: int = -390
PULL_MESSAGES_Y_POSITION: int = 370
RTP_ALIGNMENT: str = "left"
RTP_X_POSITION: int = -390
RTP_Y_POSITION: int = -380

# Logger configuration
LOGGER_ON: bool = True
LOGGER_SIMPLE_MODE: bool = True  # Set as False to use detailed log mode
LOG_DIRECTORY: str = "../logs"  # Directory to store logs

# Icon configuration
ICON_FILE_PNG: str = "slot_machine_logo.png"
ICON_FILE_ICO: str = "slot_machine_logo.ico"
