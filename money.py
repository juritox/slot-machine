from turtle import Turtle

MONEY_ALIGNMENT = "center"
MONEY_FONT = ("Courier", 20, "bold")
MONEY_X_POSITION = 0
MONEY_Y_POSITION = 360
DEFAULT_MONEY = 1000
WIN_PRIZE = 2000
PULL_COST = 50


class Money(Turtle):
    """Represents a display of money for the slot machine."""

    def __init__(self):
        """Initialize the money with its default value and position."""
        super().__init__()
        self.money = DEFAULT_MONEY
        self.win_prize = WIN_PRIZE
        self.pull_cost = PULL_COST
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(MONEY_X_POSITION, MONEY_Y_POSITION)
        self.update_money()

    def update_money(self):
        """Update the display of money."""
        self.clear()
        if self.money < self.pull_cost:
            self.color("red")
        else:
            self.color("white")
        self.write(f"Money: {self.money}", align=MONEY_ALIGNMENT, font=MONEY_FONT)

    def increase_money(self, amount):
        """Increase money by a given amount."""
        self.money += amount

    def decrease_money(self, amount):
        """Decrease money by a given amount."""
        self.money -= amount

    def get_win_prize(self):
        """Return the win prize value."""
        return self.win_prize

    def get_pull_cost(self):
        """Return the pull cost value."""
        return self.pull_cost
