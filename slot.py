from turtle import Turtle
from typing import Optional, Union
from random import choice
from config import (
    SLOT_ALIGNMENT, SLOT_FONT_SIZE, SLOT_FONT,
    TOP_SECONDARY_SLOT, BOTTOM_SECONDARY_SLOT,
    SLOT_SYMBOLS, SLOT_NUMBERS, USE_SYMBOLS
)


class Slot(Turtle):
    """Represents a slot and its value and position."""

    def __init__(self, x_position: float, y_position: float, color: str, secondary_slot: Optional[str]) -> None:
        """Initialize the slot with its value and position."""
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.values: list[Union[str, int]] = SLOT_SYMBOLS if USE_SYMBOLS else SLOT_NUMBERS
        self.value: Optional[Union[str, int]] = choice(self.values) if secondary_slot is None else None
        self.goto(x_position, y_position - SLOT_FONT_SIZE / 2 - SLOT_FONT_SIZE / 4)

    def update_slot(self, secondary_slot: Optional[str] = None,
                    main_slot_value: Optional[Union[str, int]] = None) -> None:
        """Update the slot's display with its current value. Adjust secondary slots accordingly."""
        self.clear()
        if secondary_slot == TOP_SECONDARY_SLOT:
            index = (self.values.index(main_slot_value) + 1) % len(self.values)
            self.value = self.values[index]
        elif secondary_slot == BOTTOM_SECONDARY_SLOT:
            index = (self.values.index(main_slot_value) - 1) % len(self.values)
            self.value = self.values[index]
        self.write(f"{self.value}", align=SLOT_ALIGNMENT, font=SLOT_FONT)

    def randomize_slot(self) -> None:
        self.value = choice(self.values)

    def get_value(self) -> Union[str, int]:
        """Return the slot value."""
        return self.value
