from turtle import Turtle

INSTRUCTIONS_ALIGNMENT = "center"
INSTRUCTIONS_FONT = ("Arial", 30, "bold")
INSTRUCTIONS_X_POSITION = 0
INSTRUCTIONS_Y_POSITION = -300
DEFAULT_INSTRUCTIONS = "Press SPACE to pull!\n"
HOW_TO_EXIT = "Press Escape to exit the game."
HOW_TO_EXIT_FONT = ("Arial", 14, "normal")
MESSAGES_ALIGNMENT = "center"
MESSAGES_FONT = ("Arial", 25, "bold")
MESSAGES_X_POSITION = 0
MESSAGES_Y_POSITION = 280


class Messages(Turtle):
    """Represents a display of messages for the slot machine."""

    def __init__(self):
        """Initialize messages text and position."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(MESSAGES_X_POSITION, MESSAGES_Y_POSITION)

    def player_won_message(self, won_amount):
        """Display the amount that a player wins."""
        self.clear()
        self.write(f"You  won {won_amount}!", align=MESSAGES_ALIGNMENT, font=MESSAGES_FONT)

    def player_lost_message(self, lost_amount):
        """Display the amount that a player lost."""
        self.clear()
        self.write(f"You lost {lost_amount}!", align=MESSAGES_ALIGNMENT, font=MESSAGES_FONT)


class Instructions(Turtle):
    """Represents a display of instructions for the slot machine."""

    def __init__(self):
        """Initialize instructions text and position."""
        super().__init__()
        self.instructions = DEFAULT_INSTRUCTIONS
        self.how_to_exit = HOW_TO_EXIT
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(INSTRUCTIONS_X_POSITION, INSTRUCTIONS_Y_POSITION)
        self.show_instructions()

    def show_instructions(self):
        """Update the display of instructions."""
        self.write(f"{self.instructions}", align=INSTRUCTIONS_ALIGNMENT, font=INSTRUCTIONS_FONT)
        self.write(f"{self.how_to_exit}", align=INSTRUCTIONS_ALIGNMENT, font=HOW_TO_EXIT_FONT)

    def hide_instructions(self):
        """Clear the instructions text from the screen."""
        self.clear()
