from turtle import Turtle
from random import randint

SLOT_ALIGNMENT = "center"
SLOT_FONT_SIZE = 50
SLOT_FONT = ("Courier", SLOT_FONT_SIZE, "bold")
TOP_SECONDARY_SLOT = "top"
BOTTOM_SECONDARY_SLOT = "bottom"


class Slot(Turtle):
    """Represents a slot and its value and position."""

    def __init__(self, x_position, y_position, color, secondary_slot):
        """Initialize the slot with its value and position."""
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        if secondary_slot == TOP_SECONDARY_SLOT:
            self.value = None
        elif secondary_slot == BOTTOM_SECONDARY_SLOT:
            self.value = None
        else:
            self.value = randint(0, 9)
        self.goto(x_position, y_position - SLOT_FONT_SIZE / 2 - SLOT_FONT_SIZE / 4)

    def update_slot(self, secondary_slot=None, primary_slot_value=None):
        """Update the slot's display with its current value. Adjust secondary slots accordingly."""
        self.clear()
        if secondary_slot == TOP_SECONDARY_SLOT:
            if primary_slot_value == 9:
                self.value = 0
            else:
                self.value = primary_slot_value + 1
        if secondary_slot == BOTTOM_SECONDARY_SLOT:
            if primary_slot_value == 0:
                self.value = 9
            else:
                self.value = primary_slot_value - 1
        self.write(f"{self.value}", align=SLOT_ALIGNMENT, font=SLOT_FONT)

    def randomize_slot(self):
        self.value = randint(0, 9)

    def get_value(self):
        """Return the slot value."""
        return self.value
