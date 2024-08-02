from turtle import Turtle
from config import (
    MONEY_ALIGNMENT, MONEY_FONT, DEFAULT_MONEY_COLOR, LOW_MONEY_COLOR,
    MONEY_X_POSITION, MONEY_Y_POSITION, DEFAULT_MONEY, WIN_PRIZE, PULL_COST
)


class Money(Turtle):
    """Represents a display of money for the slot machine."""

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

    def update_money(self) -> None:
        """Update the display of money."""
        self.clear()
        if self.money < self.pull_cost:
            self.color(LOW_MONEY_COLOR)
        else:
            self.color(DEFAULT_MONEY_COLOR)
        self.write(f"Money: {self.money}", align=MONEY_ALIGNMENT, font=MONEY_FONT)

    def increase_money(self, amount: int) -> None:
        """Increase money by a given amount."""
        self.money += amount

    def decrease_money(self, amount: int) -> None:
        """Decrease money by a given amount."""
        self.money -= amount

    def get_win_prize(self) -> int:
        """Return the win prize value."""
        return self.win_prize

    def get_pull_cost(self) -> int:
        """Return the pull cost value."""
        return self.pull_cost
