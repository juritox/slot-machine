from turtle import Turtle
from typing import Optional
from slot import Slot
from money import Money
from messages import Instructions, Messages
from random import randint
from config import (
    DEFAULT_SLOT_SIZE, NUMBER_OF_SLOTS, SLOT_SHAPE,
    VERTICAL_SHAPE_STRETCH, HORIZONTAL_SHAPE_STRETCH, OUTLINE_SIZE,
    STARTING_Y_POSITION, TOP_SECONDARY_SLOT, BOTTOM_SECONDARY_SLOT,
    MAIN_SLOT_COLOR, SECONDARY_SLOT_COLOR, MAIN_SLOT_OUTLINE_COLOR,
    SECONDARY_SLOT_OUTLINE_COLOR, MAIN_SLOT_DISPLAY_COLOR,
    SECONDARY_SLOT_DISPLAY_COLOR, MIN_PULL_CYCLES, MAX_PULL_CYCLES
)


class Machine:
    """Represents a slot machine with slots arranged in a specific pattern."""

    def __init__(self, money: Money, instructions: Instructions, messages: Messages) -> None:
        """Initialize the machine with slots and create the machine."""
        self.money: Money = money
        self.instructions: Instructions = instructions
        self.messages: Messages = messages
        self.main_slots: list[Slot] = []
        self.top_secondary_slots: list[Slot] = []
        self.bottom_secondary_slots: list[Slot] = []
        self.processing: bool = False
        self.create_machine()

    def create_machine(self) -> None:
        """Create the graphics for a slot machine with main slots and top and bottom secondary slots."""
        # Calculate the width and height of one slot
        slot_width = DEFAULT_SLOT_SIZE * HORIZONTAL_SHAPE_STRETCH
        slot_height = DEFAULT_SLOT_SIZE * VERTICAL_SHAPE_STRETCH

        # Calculate the total width of all slots
        total_width = slot_width * NUMBER_OF_SLOTS

        # Calculate the centered starting x position
        starting_x_position = -total_width / 2 + slot_width / 2

        # Calculate the vertical positions for top and bottom slots
        top_y_position = STARTING_Y_POSITION + slot_height
        bottom_y_position = STARTING_Y_POSITION - slot_height

        for slot in range(NUMBER_OF_SLOTS):
            # Adding top secondary slots
            self.add_slot(starting_x_position + slot * slot_width, top_y_position,
                          SECONDARY_SLOT_DISPLAY_COLOR, secondary_slot=TOP_SECONDARY_SLOT)
            # Adding bottom secondary slots
            self.add_slot(starting_x_position + slot * slot_width, bottom_y_position,
                          SECONDARY_SLOT_DISPLAY_COLOR, secondary_slot=BOTTOM_SECONDARY_SLOT)

        for slot in range(NUMBER_OF_SLOTS):
            # Adding main slots
            self.add_slot(starting_x_position + slot * slot_width, STARTING_Y_POSITION, MAIN_SLOT_DISPLAY_COLOR)

    def add_slot(self, x_position: float, y_position: float, color: str, secondary_slot: Optional[str] = None) -> None:
        """Add a slot to the machine.
        Param secondary_slot can be TOP_SECONDARY_SLOT or BOTTOM_SECONDARY_SLOT to create respective secondary slots.
        """
        new_slot_graphics = Turtle()
        new_slot_graphics.shape(SLOT_SHAPE)
        new_slot_graphics.shapesize(VERTICAL_SHAPE_STRETCH, HORIZONTAL_SHAPE_STRETCH, OUTLINE_SIZE)
        new_slot_graphics.penup()
        new_slot_graphics.setx(x_position)
        new_slot_graphics.sety(y_position)

        new_slot = Slot(x_position, y_position, color, secondary_slot)

        if secondary_slot == TOP_SECONDARY_SLOT:
            new_slot_graphics.color(SECONDARY_SLOT_COLOR, SECONDARY_SLOT_OUTLINE_COLOR)
            self.top_secondary_slots.append(new_slot)
        elif secondary_slot == BOTTOM_SECONDARY_SLOT:
            new_slot_graphics.color(SECONDARY_SLOT_COLOR, SECONDARY_SLOT_OUTLINE_COLOR)
            self.bottom_secondary_slots.append(new_slot)
        else:
            new_slot_graphics.color(MAIN_SLOT_COLOR, MAIN_SLOT_OUTLINE_COLOR)
            self.main_slots.append(new_slot)

    def update_slots(self) -> None:
        """Update all machine slots."""
        for slot in self.main_slots:
            slot.update_slot()

        for index, slot in enumerate(self.top_secondary_slots):
            value = self.main_slots[index].get_value()
            slot.update_slot(secondary_slot=TOP_SECONDARY_SLOT, main_slot_value=value)

        for index, slot in enumerate(self.bottom_secondary_slots):
            value = self.main_slots[index].get_value()
            slot.update_slot(secondary_slot=BOTTOM_SECONDARY_SLOT, main_slot_value=value)

    def pull(self) -> None:
        """Simulate pull of the machine. Generate new random slot values."""
        if self.processing:
            return

        self.processing = True

        try:
            pull_cycles = randint(MIN_PULL_CYCLES, MAX_PULL_CYCLES)
            self.instructions.hide_instructions()
            self.messages.remove_messages()

            for _ in range(pull_cycles):
                for slot in self.main_slots:
                    slot.randomize_slot()
                self.update_slots()

            if self.check_winning():
                self.money.increase_money(self.money.get_win_prize())
                self.messages.player_won_message(self.money.get_win_prize())
            else:
                self.money.decrease_money(self.money.get_pull_cost())
                self.messages.player_lost_message(self.money.get_pull_cost())

            self.money.update_money()
            self.instructions.show_instructions()

        finally:
            self.processing = False

    def check_winning(self) -> bool:
        """Check if all the slots have the same value so player wins or loses."""
        first_slot = self.main_slots[0]
        for slot in self.main_slots[1:]:
            if slot.get_value() != first_slot.get_value():
                return False
        return True
