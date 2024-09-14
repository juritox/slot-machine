"""
This module defines the Money class, which manages the player's money in the slot machine game.

The Money class extends the Turtle class to provide graphical representation
of the player's current money, and handles operations like increasing and
decreasing the money amount.
"""

from turtle import Turtle
from slot import get_slot_values
from config import (
    MONEY_ALIGNMENT, MONEY_FONT, DEFAULT_MONEY_COLOR, LOW_MONEY_COLOR,
    MONEY_X_POSITION, MONEY_Y_POSITION, DEFAULT_MONEY, WIN_PRIZE, PULL_COST,
    MONEY_MESSAGES_FONT, PRIZE_MESSAGES_ALIGNMENT, PULL_MESSAGES_ALIGNMENT,
    PRIZE_MESSAGES_X_POSITION, PRIZE_MESSAGES_Y_POSITION, USE_SYMBOLS,
    PULL_MESSAGES_X_POSITION, PULL_MESSAGES_Y_POSITION, JACKPOT_ENABLED,
    JACKPOT_WINNING_SYMBOL, JACKPOT_WINNING_NUMBER, JACKPOT_PRIZE_MULTIPLIER,
    JACKPOT_X_POSITION, JACKPOT_Y_POSITION, NUMBER_OF_SLOTS,
    RTP_ALIGNMENT, RTP_X_POSITION, RTP_Y_POSITION
)


class Money(Turtle):
    """
    Represents the money display and management for the slot machine.

    This class extends the Turtle class to provide graphical representation
    and manages the player's money, win prize, pull cost and jackpot.

    Attributes:
        _money (int): The current amount of money the player has.
        _win_prize (int): The amount of money won for a successful pull.
        _pull_cost (int): The cost of each pull.
        _symbols_used (bool): Flag signaling if symbols are used in slots, otherwise numbers are used.
        _jackpot_enabled (bool): Flag signaling if jackpot is enabled or disabled.
        _jackpot_multiplier (int): Number by which the prize would be multiplied if jackpot is hit.
        _jackpot_winning_symbol (str): Jackpot winning symbol if slots are using symbols.
        _jackpot_winning_number (int): Jackpot winning number if slots are using numbers.
    """

    def __init__(self) -> None:
        """
        Initialize the money with its default value and position.
        """
        super().__init__()
        self._money: int = DEFAULT_MONEY
        self._win_prize: int = WIN_PRIZE
        self._pull_cost: int = PULL_COST
        self._symbols_used: bool = USE_SYMBOLS
        self._jackpot_enabled: bool = JACKPOT_ENABLED
        self._jackpot_multiplier: int = JACKPOT_PRIZE_MULTIPLIER
        self._jackpot_winning_symbol: str = JACKPOT_WINNING_SYMBOL
        self._jackpot_winning_number: int = JACKPOT_WINNING_NUMBER
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
        return f"Money: {self._money}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Money object.

        Returns:
            str: A string representation of the Money object.
        """
        return f"Money(money={self._money}, win_prize={self._win_prize}, pull_cost={self._pull_cost})"

    @property
    def money(self) -> int:
        """
        Get the current amount of money.

        Returns:
            int: The current amount of money.
        """
        return self._money

    @money.setter
    def money(self, new_amount: int) -> None:
        """
        Set the current amount of money.

        Args:
            new_amount (int): The new amount of money.
        """
        self._money = new_amount

    @property
    def win_prize(self) -> int:
        """
        Get the current win prize amount.

        Returns:
            int: The current win prize amount.
        """
        return self._win_prize

    @property
    def pull_cost(self) -> int:
        """
        Get the current pull cost.

        Returns:
            int: The current pull cost.
        """
        return self._pull_cost

    @property
    def symbols_used(self) -> bool:
        """
        Get the symbols used flag.

        Returns:
            bool: The symbols used flag.
        """
        return self._symbols_used

    @property
    def jackpot_enabled(self) -> bool:
        """
        Get the jackpot enabled flag.

        Returns:
            bool: The jackpot enabled flag.
        """
        return self._jackpot_enabled

    @property
    def jackpot_multiplier(self) -> int:
        """
        Get the jackpot multiplier.

        Returns:
            int: The jackpot multiplier.
        """
        return self._jackpot_multiplier

    @property
    def jackpot_winning_symbol(self) -> str:
        """
        Get the jackpot winning symbol.

        Returns:
            str: The jackpot winning symbol.
        """
        return self._jackpot_winning_symbol

    @property
    def jackpot_winning_number(self) -> int:
        """
        Get the jackpot winning number.

        Returns:
            int: The jackpot winning number.
        """
        return self._jackpot_winning_number

    @staticmethod
    def calculate_jackpot_chance() -> float:
        """
        Calculate the chance of winning a jackpot.

        Returns:
            float: The jackpot winning chance.
        """
        number_of_values = len(get_slot_values())

        chance = 1 / (number_of_values ** NUMBER_OF_SLOTS)

        return chance

    @staticmethod
    def calculate_loss_chance() -> float:
        """
        Calculate the chance of losing.
        Returns:
            float: The losing chance.
        """
        number_of_values = len(get_slot_values())

        chance = 1 - number_of_values / (number_of_values ** NUMBER_OF_SLOTS)

        return chance

    @staticmethod
    def calculate_win_chance() -> float:
        """
        Calculate the chance of winning (including jackpot if enabled).

        Returns:
            float: The winning chance.
        """
        number_of_values = len(get_slot_values())

        chance = number_of_values / (number_of_values ** NUMBER_OF_SLOTS)

        return chance

    def calculate_regular_win_chance(self) -> float:
        """
        Calculate the chance of winning without hitting the jackpot.

        Returns:
            float: The regular winning chance.
        """
        if self.jackpot_enabled:
            chance = self.calculate_win_chance() - self.calculate_jackpot_chance()
        else:
            chance = self.calculate_win_chance()

        return chance

    def calculate_rtp(self) -> float:
        """
        Calculate the Return to Player (RTP) for the slot machine.

        Returns:
            float: The RTP as a percentage.
        """
        if self.jackpot_enabled:
            regular_win_chance = self.calculate_regular_win_chance()
            jackpot_chance = self.calculate_jackpot_chance()
            expected_regular_return = regular_win_chance * self.win_prize
            expected_jackpot_return = jackpot_chance * self.win_prize * self.jackpot_multiplier
            total_expected_return = expected_regular_return + expected_jackpot_return
        else:
            win_chance = self.calculate_win_chance()
            total_expected_return = win_chance * self.win_prize

        # RTP is the ratio of expected return to the amount bet (pull cost)
        rtp = (total_expected_return / self.pull_cost) * 100

        return rtp

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

    def update_money(self) -> None:
        """
        Update the display of money on the screen.
        """
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
        self.show_rtp()

    def show_win_prize(self) -> None:
        """
        Display the current win prize on the screen.
        """
        self.goto(PRIZE_MESSAGES_X_POSITION, PRIZE_MESSAGES_Y_POSITION)
        self.write(f"Win prize: ${self.win_prize}",
                   align=PRIZE_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)

    def show_pull_cost(self) -> None:
        """
        Display the current pull cost on the screen.
        """
        self.goto(PULL_MESSAGES_X_POSITION, PULL_MESSAGES_Y_POSITION)
        self.write(f"Pull cost: ${self.pull_cost}",
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
            symbol_or_number = self.jackpot_winning_symbol
            jackpot_label = "Jackpot symbol:"
        else:
            symbol_or_number = str(self.jackpot_winning_number)
            jackpot_label = "Jackpot number:"

        # Display the jackpot text in a larger font
        self.write(symbol_or_number, align=PRIZE_MESSAGES_ALIGNMENT, font=large_font)
        # Move to a new line for the rest of the text
        self.goto(JACKPOT_X_POSITION, JACKPOT_Y_POSITION - line_spacing)
        # Display the jackpot information in the original font
        jackpot_info = f"{jackpot_label} \nJackpot multiplier: ×{self.jackpot_multiplier}"
        self.write(jackpot_info, align=PRIZE_MESSAGES_ALIGNMENT, font=MONEY_MESSAGES_FONT)

    def show_rtp(self):
        """
        Display the current Return To Player (RPT) percentage.
        """
        self.goto(RTP_X_POSITION, RTP_Y_POSITION)
        self.write(f"RTP:\n{round(self.calculate_rtp(), 2)}%",
                   align=RTP_ALIGNMENT, font=MONEY_MESSAGES_FONT)
