"""
This module defines the Money class, which manages the player's money in the slot machine game.

The Money class extends the Turtle class to provide graphical representation
of the player's current money, and handles operations like increasing and
decreasing the money amount.
"""

from turtle import Turtle
from config.config import (
    MONEY_ALIGNMENT, MONEY_FONT, DEFAULT_MONEY_COLOR, LOW_MONEY_COLOR,
    MONEY_X_POSITION, MONEY_Y_POSITION, DEFAULT_MONEY, WIN_PRIZE, PULL_COST,
    MONEY_MESSAGES_FONT, PRIZE_MESSAGES_ALIGNMENT, PULL_MESSAGES_ALIGNMENT,
    PRIZE_MESSAGES_X_POSITION, PRIZE_MESSAGES_Y_POSITION, USE_SYMBOLS,
    PULL_MESSAGES_X_POSITION, PULL_MESSAGES_Y_POSITION, JACKPOT_ENABLED,
    JACKPOT_WINNING_SYMBOL, JACKPOT_WINNING_NUMBER, JACKPOT_PRIZE_MULTIPLIER,
    JACKPOT_X_POSITION, JACKPOT_Y_POSITION
)


class Money(Turtle):
    """
    Represents the money display and management for the slot machine.

    This class extends the Turtle class to provide graphical representation
    and manages the player's money, win prize, pull cost and jackpot.

    Attributes:
        money (int): The current amount of money the player has.
        win_prize (int): The amount of money won for a successful pull.
        pull_cost (int): The cost of each pull.
        symbols_used (bool): Flag signaling if symbols are used in slots, otherwise numbers are used.
        jackpot_enabled (bool): Flag signaling if jackpot is enabled or disabled.
        jackpot_multiplier (int): Number by which the prize would be multiplied if jackpot is hit.
        jackpot_winning_symbol (str): Jackpot winning symbol if slots are using symbols.
        jackpot_winning_number (int): Jackpot winning number if slots are using numbers.
    """

    def __init__(self) -> None:
        """Initialize the money with its default value and position."""
        super().__init__()
        self.money: int = DEFAULT_MONEY
        self.win_prize: int = WIN_PRIZE
        self.pull_cost: int = PULL_COST
        self.symbols_used: bool = USE_SYMBOLS
        self.jackpot_enabled: bool = JACKPOT_ENABLED
        self.jackpot_multiplier: int = JACKPOT_PRIZE_MULTIPLIER
        self.jackpot_winning_symbol: str = JACKPOT_WINNING_SYMBOL
        self.jackpot_winning_number: int = JACKPOT_WINNING_NUMBER
        self.color(DEFAULT_MONEY_COLOR)
        self.penup()
        self.speed(0)
        self.hideturtle()
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
        self.goto(MONEY_X_POSITION, MONEY_Y_POSITION)
        if self.money < self.pull_cost:
            self.color(LOW_MONEY_COLOR)
        else:
            self.color(DEFAULT_MONEY_COLOR)
        self.write(f"Money: ${self.money}", align=MONEY_ALIGNMENT, font=MONEY_FONT)
        self.show_pull_cost()
        self.show_win_prize()
        self.color(DEFAULT_MONEY_COLOR)
        self.show_jackpot()

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

    def show_win_prize(self) -> None:
        """
        Display the current win prize on the screen.
        """
        self.goto(PRIZE_MESSAGES_X_POSITION, PRIZE_MESSAGES_Y_POSITION)
        self.write(f"Win prize: ${self.get_win_prize()}",
                   align=PRIZE_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)

    def show_pull_cost(self) -> None:
        """
        Display the current pull cost on the screen.
        """
        self.goto(PULL_MESSAGES_X_POSITION, PULL_MESSAGES_Y_POSITION)
        self.write(f"Pull cost: ${self.get_pull_cost()}",
                   align=PULL_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)

    def show_jackpot(self) -> None:
        """
        Display the jackpot symbol or number and jackpot prize multiplier on the screen.
        If jackpot is disabled then it shows "JACKPOT DISABLED" instead.
        """
        self.goto(JACKPOT_X_POSITION, JACKPOT_Y_POSITION)

        # Define larger font size for the jackpot message
        large_font_size = MONEY_MESSAGES_FONT[1] * 2
        large_font = (MONEY_FONT[0], large_font_size, MONEY_FONT[2])
        # Define spacing for moving to a new line
        line_spacing = large_font_size / 2 + large_font_size / 4

        if not self.jackpot_enabled:
            self.write("JACKPOT DISABLED", align=PRIZE_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)
            return

        # Determine the jackpot text and label based on symbols_used
        if self.symbols_used:
            symbol_or_number = self.get_jackpot_winning_symbol()
            jackpot_label = "Jackpot symbol:"
        else:
            symbol_or_number = str(self.get_jackpot_winning_number())
            jackpot_label = "Jackpot number:"

        # Display the jackpot text in a larger font
        self.write(symbol_or_number, align=PRIZE_MESSAGES_ALIGNMENT, font=large_font)
        # Move to a new line for the rest of the text
        self.goto(JACKPOT_X_POSITION, JACKPOT_Y_POSITION - line_spacing)
        # Display the jackpot information in the original font
        jackpot_info = f"{jackpot_label} \nJackpot multiplier: ×{self.get_jackpot_multiplier()}"
        self.write(jackpot_info, align=PRIZE_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)

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

    def get_symbols_used(self) -> bool:
        """
        Get the symbols used flag.

        Returns:
            bool: The symbols used flag.
        """
        return self.symbols_used

    def get_jackpot_enabled(self) -> bool:
        """
        Get the jackpot enabled flag.

        Returns:
            bool: The jackpot enabled flag.
        """
        return self.jackpot_enabled

    def get_jackpot_multiplier(self) -> int:
        """
        Get the jackpot multiplier.

        Returns:
            int: The jackpot multiplier.
        """
        return self.jackpot_multiplier

    def get_jackpot_winning_symbol(self) -> str:
        """
        Get the jackpot winning symbol.

        Returns:
            str: The jackpot winning symbol.
        """
        return self.jackpot_winning_symbol

    def get_jackpot_winning_number(self) -> int:
        """
        Get the jackpot winning number.

        Returns:
            int: The jackpot winning number.
        """
        return self.jackpot_winning_number
