"""
This module defines the Slot class, which represents individual slots in a slot machine.

The Slot class extends the Turtle class to provide graphical representation
and manages the slot's value and position.
"""

from turtle import Turtle
from typing import TypeAlias
from random import choice
from config import (
    SLOT_ALIGNMENT, SLOT_FONT_SIZE, SLOT_FONT,
    TOP_SECONDARY_SLOT, BOTTOM_SECONDARY_SLOT,
    SLOT_SYMBOLS, SLOT_NUMBERS, USE_SYMBOLS
)

# Define a type alias for slot value
SlotValue: TypeAlias = str | int


class Slot(Turtle):
    """
    Represents a single slot in a slot machine.

    This class extends the Turtle class to provide graphical representation
    and manages the slot's value and position.

    Attributes:
        value (SlotValue | None): The current value displayed on the slot.
            It can be a string or an integer, or it can be None if this is a secondary slot.
        values (list[SlotValue]): The possible values for this slot, which can
            be either strings or integers.
    """

    def __init__(self, x_position: float, y_position: float, color: str, secondary_slot: str | None) -> None:
        """
        Initialize a new Slot instance.

        Args:
            x_position (float): The x-coordinate for the slot's position.
            y_position (float): The y-coordinate for the slot's position.
            color (str): The color of the slot's text.
            secondary_slot (str | None): Indicates if this is a secondary slot and its position (top or bottom).
                If None is provided, this is a main slot.
        """
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.values: list[SlotValue] = SLOT_SYMBOLS if USE_SYMBOLS else SLOT_NUMBERS  # type: ignore
        self.value: SlotValue | None = choice(self.values) if secondary_slot is None else None
        self.goto(x_position, y_position - SLOT_FONT_SIZE / 2 - SLOT_FONT_SIZE / 4)

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Slot object.

        Returns:
            str: A string showing the slot's value.
        """
        return f"Slot: {self.value}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Slot object.

        Returns:
            str: A string representation of the Slot object.
        """
        return (f"Slot(x_position={self.xcor():.2f}, "
                f"y_position={self.ycor():.2f}, "
                f"color={self.color()[0]}, "
                f"value={self.value})")

    def update_slot(self, secondary_slot: str | None = None,
                    main_slot_value: SlotValue | None = None) -> None:
        """
        Update the slot's display with its current value.

        If this is a secondary slot, it updates based on the primary slot's value.

        Args:
            secondary_slot (str | None): Indicates if this is a secondary slot and its position (top or bottom).
            main_slot_value (SlotValue | None): The value of the primary slot, if applicable.
        """
        self.clear()
        if secondary_slot == TOP_SECONDARY_SLOT and main_slot_value is not None:
            index = (self.values.index(main_slot_value) + 1) % len(self.values)
            self.value = self.values[index]
        elif secondary_slot == BOTTOM_SECONDARY_SLOT and main_slot_value is not None:
            index = (self.values.index(main_slot_value) - 1) % len(self.values)
            self.value = self.values[index]
        if self.value is not None:
            self.write(f"{self.value}", align=SLOT_ALIGNMENT, font=SLOT_FONT)

    def randomize_slot(self) -> None:
        """Randomly select a new value for the slot."""
        self.value = choice(self.values)

    def get_value(self) -> SlotValue | None:
        """
        Get the current value of the slot.

        Returns:
            SlotValue | None: The current value displayed on the slot.
        """
        return self.value
