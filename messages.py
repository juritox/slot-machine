from turtle import Turtle
from config import (
    INSTRUCTIONS_ALIGNMENT, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR,
    INSTRUCTIONS_X_POSITION, INSTRUCTIONS_Y_POSITION,
    DEFAULT_INSTRUCTIONS, HOW_TO_EXIT, HOW_TO_EXIT_FONT,
    MESSAGES_ALIGNMENT, MESSAGES_FONT, MESSAGES_COLOR,
    MESSAGES_X_POSITION, MESSAGES_Y_POSITION
)


class Messages(Turtle):
    """Represents a display of messages for the slot machine."""

    def __init__(self) -> None:
        """Initialize messages text and position."""
        super().__init__()
        self.color(MESSAGES_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(MESSAGES_X_POSITION, MESSAGES_Y_POSITION)

    def player_won_message(self, won_amount: int) -> None:
        """Display the amount that a player wins."""
        self.clear()
        self.write(f"You  won {won_amount}!", align=MESSAGES_ALIGNMENT, font=MESSAGES_FONT)

    def player_lost_message(self, lost_amount: int) -> None:
        """Display the amount that a player lost."""
        self.clear()
        self.write(f"You lost {lost_amount}!", align=MESSAGES_ALIGNMENT, font=MESSAGES_FONT)

    def remove_messages(self) -> None:
        """Clear the messages text from the screen."""
        self.clear()


class Instructions(Turtle):
    """Represents a display of instructions for the slot machine."""

    def __init__(self) -> None:
        """Initialize instructions text and position."""
        super().__init__()
        self.instructions: str = DEFAULT_INSTRUCTIONS
        self.how_to_exit: str = HOW_TO_EXIT
        self.color(INSTRUCTIONS_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(INSTRUCTIONS_X_POSITION, INSTRUCTIONS_Y_POSITION)
        self.show_instructions()

    def show_instructions(self) -> None:
        """Update the display of instructions."""
        self.write(f"{self.instructions}", align=INSTRUCTIONS_ALIGNMENT, font=INSTRUCTIONS_FONT)
        self.write(f"{self.how_to_exit}", align=INSTRUCTIONS_ALIGNMENT, font=HOW_TO_EXIT_FONT)

    def hide_instructions(self) -> None:
        """Clear the instructions text from the screen."""
        self.clear()
