"""
This module defines the Messages and Instructions classes for displaying game information.

These classes extend the Turtle class to provide graphical representation
of game messages and instructions to the player.
"""

from turtle import Turtle
from money import Money
from config import (
    INSTRUCTIONS_ALIGNMENT, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR,
    INSTRUCTIONS_X_POSITION, INSTRUCTIONS_Y_POSITION,
    DEFAULT_INSTRUCTIONS, HOW_TO_EXIT, HOW_TO_EXIT_FONT,
    MAIN_MESSAGES_ALIGNMENT, MAIN_MESSAGES_FONT, MESSAGES_COLOR,
    MAIN_MESSAGES_X_POSITION, MAIN_MESSAGES_Y_POSITION
)


class Messages(Turtle):
    """
    Represents the message display for the slot machine.

    This class extends the Turtle class to provide graphical representation
    of game messages.
    """

    def __init__(self) -> None:
        """Initialize the Messages object with default position and color."""
        super().__init__()
        self.color(MESSAGES_COLOR)
        self.penup()
        self.hideturtle()

    def __repr__(self) -> str:
        """
        Return a string representation of the Messages object.

        Returns:
            str: A string representation of the Messages object.
        """
        return f"Messages(x={self.xcor():.2f}, y={self.ycor():.2f}, color={self.color()[0]})"

    def player_won_message(self, won_amount: int) -> None:
        """
        Display a message indicating the player has won.

        Args:
            won_amount (int): The amount of money the player won.
        """
        self.clear()
        self.goto(MAIN_MESSAGES_X_POSITION, MAIN_MESSAGES_Y_POSITION)
        self.write(f"You  won {won_amount}!", align=MAIN_MESSAGES_ALIGNMENT, font=MAIN_MESSAGES_FONT)

    def player_lost_message(self, lost_amount: int) -> None:
        """
        Display a message indicating the player has lost.

        Args:
            lost_amount (int): The amount of money the player lost.
        """
        self.clear()
        self.goto(MAIN_MESSAGES_X_POSITION, MAIN_MESSAGES_Y_POSITION)
        self.write(f"You lost {lost_amount}!", align=MAIN_MESSAGES_ALIGNMENT, font=MAIN_MESSAGES_FONT)

    def remove_messages(self) -> None:
        """Clear all messages from the screen."""
        self.clear()


class Instructions(Turtle):
    """
    Represents the instructions display for the slot machine.

    This class extends the Turtle class to provide graphical representation
    of game instructions.
    """

    def __init__(self) -> None:
        """Initialize the Instructions object with default text and position."""
        super().__init__()
        self.instructions: str = DEFAULT_INSTRUCTIONS
        self.how_to_exit: str = HOW_TO_EXIT
        self.color(INSTRUCTIONS_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(INSTRUCTIONS_X_POSITION, INSTRUCTIONS_Y_POSITION)
        self.show_instructions()

    def __repr__(self) -> str:
        """
        Return a string representation of the Instructions object.

        Returns:
            str: A string representation of the Instructions object.
        """
        return (f"Instructions(x={self.xcor():.2f}, y={self.ycor():.2f}, color={self.color()[0]}, "
                f"instructions={self.instructions}, how_to_exit={self.how_to_exit})")

    def show_instructions(self) -> None:
        """Display the game instructions on the screen."""
        self.write(f"{self.instructions}", align=INSTRUCTIONS_ALIGNMENT, font=INSTRUCTIONS_FONT)
        self.write(f"{self.how_to_exit}", align=INSTRUCTIONS_ALIGNMENT, font=HOW_TO_EXIT_FONT)

    def hide_instructions(self) -> None:
        """Clear the instructions from the screen."""
        self.clear()
