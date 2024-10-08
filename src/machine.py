"""
This module defines the Machine class, which represents the entire slot machine.

The Machine class manages the collection of slots, handles the pull mechanism,
and determines winning conditions.
"""

from turtle import Turtle
from random import randint
from slot import Slot
from money import Money
from messages import Instructions, Messages
from logger import Logger, loggable
from config import (
    DEFAULT_SLOT_SIZE, NUMBER_OF_SLOTS, SLOT_SHAPE,
    VERTICAL_SHAPE_STRETCH, HORIZONTAL_SHAPE_STRETCH, OUTLINE_SIZE,
    STARTING_Y_POSITION, TOP_SECONDARY_SLOT, BOTTOM_SECONDARY_SLOT,
    MAIN_SLOT_COLOR, SECONDARY_SLOT_COLOR, MAIN_SLOT_OUTLINE_COLOR,
    SECONDARY_SLOT_OUTLINE_COLOR, MAIN_SLOT_DISPLAY_COLOR,
    SECONDARY_SLOT_DISPLAY_COLOR, MIN_PULL_CYCLES, MAX_PULL_CYCLES,
    FRAME_COLOR, FRAME_PADDING_FACTOR, FRAME_PEN_SIZE
)


class Machine:
    """
    Represents the entire slot machine.

    This class manages the collection of slots, handles the pull mechanism,
    and determines winning conditions.

    Attributes:
        money (Money): The money management object for this machine.
        instructions (Instructions): The instructions display object.
        messages (Messages): The messages display object.
        main_slots (list[Slot]): The list of main slot objects.
        top_secondary_slots (list[Slot]): The list of top secondary slot objects.
        bottom_secondary_slots (list[Slot]): The list of bottom secondary slot objects.
        processing (bool): Indicates whether the machine is currently processing a pull.
    """

    def __init__(self, money: Money, instructions: Instructions, messages: Messages, logger: Logger) -> None:
        """
        Initialize a new Machine instance.

        Args:
            money (Money): The money management object for this machine.
            instructions (Instructions): The instructions display object.
            messages (Messages): The messages display object.
        """
        self.money: Money = money
        self.instructions: Instructions = instructions
        self.messages: Messages = messages
        self.logger: Logger = logger
        self.main_slots: list[Slot] = []
        self.top_secondary_slots: list[Slot] = []
        self.bottom_secondary_slots: list[Slot] = []
        self.processing: bool = False
        self.create_machine()

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Machine object.

        Returns:
            str: A string showing the current state of the main slots.
        """
        slot_values = [slot.value for slot in self.main_slots]
        return f"Machine: {slot_values}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Machine object.

        Returns:
            str: A string representation of the Machine object.
        """
        return f"Machine(slots={len(self.main_slots)}, processing={self.processing})"

    @loggable(lambda self, *args, **kwargs: self.logger)
    def create_machine(self) -> None:
        """
        Create the graphics for the slot machine with main and secondary slots,
        including a frame around the slots.
        """
        self.logger.log("Creating the slot machine with frame.")
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

        # Calculate frame dimensions
        total_height = slot_height * 3  # For top, main, and bottom slots
        frame_padding = slot_width * FRAME_PADDING_FACTOR
        frame_width = total_width + frame_padding * 2
        frame_height = total_height + frame_padding * 2

        # Calculate the centered frame position
        frame_x = -frame_width / 2
        frame_y = STARTING_Y_POSITION - total_height / 2 - frame_padding

        # Create the frame
        self.create_frame(frame_x, frame_y, frame_width, frame_height)

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

    @loggable(lambda self, *args, **kwargs: self.logger)
    def create_frame(self, x: float, y: float, width: float, height: float) -> None:
        """
        Create a frame around the slots.

        Args:
            x (float): The x-coordinate of the bottom-left corner of the frame.
            y (float): The y-coordinate of the bottom-left corner of the frame.
            width (float): The width of the frame.
            height (float): The height of the frame.
        """
        self.logger.log(f"Creating frame at ({x}, {y}) with dimensions {width}x{height}")
        frame = Turtle()
        frame.hideturtle()
        frame.penup()
        frame.goto(x, y)
        frame.pendown()
        frame.color(FRAME_COLOR)
        frame.pensize(FRAME_PEN_SIZE)

        # Draw the frame
        for _ in range(2):
            frame.forward(width)
            frame.left(90)
            frame.forward(height)
            frame.left(90)

    @loggable(lambda self, *args, **kwargs: self.logger)
    def add_slot(self, x_position: float, y_position: float, color: str, secondary_slot: str | None = None) -> None:
        """
        Add a slot to the machine.

        Args:
            x_position (float): The x-coordinate for the slot's position.
            y_position (float): The y-coordinate for the slot's position.
            color (str): The color of the slot's text.
            secondary_slot (str | None): Indicates if this is a secondary slot and its position (top or bottom).
        """
        self.logger.log(f"Adding a slot at ({x_position}, {y_position}) "
                        f"with color {color} and secondary slot type {secondary_slot}")
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

    @loggable(lambda self, *args, **kwargs: self.logger)
    def update_slots(self) -> None:
        """
        Update all machine slots.
        """
        self.logger.log("Updating all slots.")
        for slot in self.main_slots:
            slot.update_slot()

        for index, slot in enumerate(self.top_secondary_slots):
            value = self.main_slots[index].value
            slot.update_slot(secondary_slot=TOP_SECONDARY_SLOT, main_slot_value=value)

        for index, slot in enumerate(self.bottom_secondary_slots):
            value = self.main_slots[index].value
            slot.update_slot(secondary_slot=BOTTOM_SECONDARY_SLOT, main_slot_value=value)

    @loggable(lambda self, *args, **kwargs: self.logger)
    def pull(self) -> None:
        """
        Simulate a pull of the slot machine.

        This method randomizes the slots, checks for winning conditions,
        and updates the player's money accordingly.
        """
        self.logger.log("Starting a pull sequence.")
        if self.money.jackpot_enabled:
            self.logger.log("Jackpot is enabled.")
        else:
            self.logger.log("Jackpot is disabled.")
        if self.processing:
            self.logger.log("Pull attempted while machine is still processing.")
            return

        self.processing = True

        try:
            pull_cost = self.money.pull_cost
            self.money.decrease_money(pull_cost)

            pull_cycles = randint(MIN_PULL_CYCLES, MAX_PULL_CYCLES)
            self.logger.log(f"Starting pull sequence with {pull_cycles} cycles.")
            self.instructions.hide_instructions()
            self.messages.remove_messages()

            for cycle in range(pull_cycles):
                for slot in self.main_slots:
                    slot.randomize_slot()
                self.update_slots()
                self.logger.log(f"Pull cycle {cycle + 1} completed.")

            if self.check_winning():
                if self.money.jackpot_enabled:
                    if self.check_jackpot():
                        jackpot_prize = self.money.win_prize * self.money.jackpot_multiplier
                        self.money.increase_money(jackpot_prize)
                        self.messages.player_won_jackpot_message(jackpot_prize - pull_cost)
                        self.logger.log(f"Player won a jackpot! Prize: ${jackpot_prize - pull_cost}")
                    else:
                        win_prize = self.money.win_prize
                        self.money.increase_money(win_prize)
                        self.messages.player_won_message(win_prize - pull_cost)
                        self.logger.log(f"Player won! Prize: ${win_prize - pull_cost}")
                else:
                    win_prize = self.money.win_prize
                    self.money.increase_money(win_prize)
                    self.messages.player_won_message(win_prize - pull_cost)
                    self.logger.log(f"Player won! Prize: ${win_prize - pull_cost}")
            else:
                self.messages.player_lost_message(pull_cost)
                self.logger.log(f"Player lost. Cost: ${pull_cost}")

            self.money.update_money()
            self.instructions.show_instructions()

        finally:
            self.processing = False
            self.logger.log("Pull sequence completed.")

    @loggable(lambda self, *args, **kwargs: self.logger)
    def check_winning(self) -> bool:
        """
        Check if the current slot configuration is a winning one.

        Returns:
            bool: True if all slots have the same value, False otherwise.
        """
        self.logger.log("Checking for a winning condition.")
        first_slot = self.main_slots[0]
        for slot in self.main_slots[1:]:
            if slot.value != first_slot.value:
                self.logger.log(f"No match found. Slot values: {[slot.value for slot in self.main_slots]}")
                return False
        self.logger.log(f"All slots matched! Slot values: {[slot.value for slot in self.main_slots]}")
        return True

    @loggable(lambda self, *args, **kwargs: self.logger)
    def check_jackpot(self) -> bool:
        """
        Check if the current slot configuration is a jackpot winning one.

        Returns:
            bool: True if all slots have the same value and the value is also a jackpot value, False otherwise.
        """
        first_slot_value = self.main_slots[0].value
        jackpot_value = (self.money.jackpot_winning_symbol
                         if self.money.symbols_used
                         else self.money.jackpot_winning_number)

        is_jackpot = first_slot_value == jackpot_value
        self.logger.log(f"Jackpot {"matched" if is_jackpot else "not matched"}. "
                        f"Jackpot value: {jackpot_value}")
        return is_jackpot
