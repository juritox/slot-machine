"""
This module defines the Money class, which manages the player's money in the slot machine game.

The Money class extends the Turtle class to provide graphical representation
of the player's current money, and handles operations like increasing and
decreasing the money amount.
"""

from turtle import Turtle
from config import (
    MONEY_ALIGNMENT, MONEY_FONT, DEFAULT_MONEY_COLOR, LOW_MONEY_COLOR,
    MONEY_X_POSITION, MONEY_Y_POSITION, DEFAULT_MONEY, WIN_PRIZE, PULL_COST
)


class Money(Turtle):
    """
    Represents the money display and management for the slot machine.

    This class extends the Turtle class to provide graphical representation
    and manages the player's money, win prize, and pull cost.

    Attributes:
        money (int): The current amount of money the player has.
        win_prize (int): The amount of money won for a successful pull.
        pull_cost (int): The cost of each pull.
    """

    def __init__(self) -> None:
        """Initialize the money with its default value and position."""
        super().__init__()
        self.money: int = DEFAULT_MONEY
        self.win_prize: int = WIN_PRIZE
        self.pull_cost: int = PULL_COST
        self.color(DEFAULT_MONEY_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(MONEY_X_POSITION, MONEY_Y_POSITION)
        self.update_money()

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Money object.

        Returns:
            str: A string showing the current amount of money.
        """
        return f"Money: {self.money}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Money object.

        Returns:
            str: A string representation of the Money object.
        """
        return f"Money(money={self.money}, win_prize={self.win_prize}, pull_cost={self.pull_cost})"

    def update_money(self) -> None:
        """Update the display of money on the screen."""
        self.clear()
        if self.money < self.pull_cost:
            self.color(LOW_MONEY_COLOR)
        else:
            self.color(DEFAULT_MONEY_COLOR)
        self.write(f"Money: {self.money}", align=MONEY_ALIGNMENT, font=MONEY_FONT)

    def increase_money(self, amount: int) -> None:
        """
        Increase the player's money by the specified amount.

        Args:
            amount (int): The amount to increase the money by.
        """
        self.money += amount

    def decrease_money(self, amount: int) -> None:
        """
        Decrease the player's money by the specified amount.

        Args:
            amount (int): The amount to decrease the money by.
        """
        self.money -= amount

    def get_win_prize(self) -> int:
        """
        Get the current win prize amount.

        Returns:
            int: The current win prize amount.
        """
        return self.win_prize

    def get_pull_cost(self) -> int:
        """
        Get the current pull cost.

        Returns:
            int: The current pull cost.
        """
        return self.pull_cost
