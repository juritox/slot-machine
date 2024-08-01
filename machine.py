from turtle import Turtle, Screen
from slot import Slot
from money import Money
from messages import Instructions, Messages
from random import randint

DEFAULT_SLOT_SIZE = 20  # Do not change this value, it is Turtle default size

NUMBER_OF_SLOTS = 3
VERTICAL_SHAPE_STRETCH = 5
HORIZONTAL_SHAPE_STRETCH = 5
OUTLINE_SIZE = 10
STARTING_Y_POSITION = 0

screen = Screen()
screen.tracer(0)
money = Money()
instructions = Instructions()
messages = Messages()


class Machine:
    """Represents a slot machine with slots arranged in a specific pattern."""

    def __init__(self):
        """Initialize the machine with slots and create the machine."""
        self.machine_slots = []
        self.top_secondary_slots = []
        self.bottom_secondary_slots = []
        self.processing = False
        self.create_machine()

    def create_machine(self):
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
            self.add_slot(starting_x_position + slot * slot_width, top_y_position, secondary_slot="top")
            # Adding bottom secondary slots
            self.add_slot(starting_x_position + slot * slot_width, bottom_y_position, secondary_slot="bottom")

        for slot in range(NUMBER_OF_SLOTS):
            # Adding main slots
            self.add_slot(starting_x_position + slot * slot_width, STARTING_Y_POSITION, color="red")

    def add_slot(self, x_position, y_position, secondary_slot=None, color="orange"):
        """
        Add a slot to the machine.
        Parameter secondary_slot can be 'top' or 'bottom' to create respective secondary slots.
        """
        new_slot_graphics = Turtle()
        new_slot_graphics.shape("square")
        new_slot_graphics.shapesize(VERTICAL_SHAPE_STRETCH, HORIZONTAL_SHAPE_STRETCH, OUTLINE_SIZE)
        new_slot_graphics.penup()
        new_slot_graphics.setx(x_position)
        new_slot_graphics.sety(y_position)

        new_slot = Slot(x_position, y_position, color, secondary_slot)

        if secondary_slot == "top":
            new_slot_graphics.color("gray", "black")
            self.top_secondary_slots.append(new_slot)
        elif secondary_slot == "bottom":
            new_slot_graphics.color("gray", "black")
            self.bottom_secondary_slots.append(new_slot)
        else:
            new_slot_graphics.color("white", "black")
            self.machine_slots.append(new_slot)

    def update_slots(self):
        """Update all machine slots."""
        for slot in self.machine_slots:
            slot.update_slot()

        for index, slot in enumerate(self.top_secondary_slots):
            value = self.machine_slots[index].get_value()
            slot.update_slot(secondary_slot="top", primary_slot_value=value)

        for index, slot in enumerate(self.bottom_secondary_slots):
            value = self.machine_slots[index].get_value()
            slot.update_slot(secondary_slot="bottom", primary_slot_value=value)

    def pull(self):
        """Simulate pull of the machine. Generate new random slot values."""
        if self.processing:
            return

        self.processing = True

        try:
            pull_cycles = randint(10, 20)

            instructions.hide_instructions()

            for _ in range(pull_cycles):
                for slot in self.machine_slots:
                    slot.randomize_slot()
                self.update_slots()

            if self.check_winning():
                money.increase_money(money.get_win_prize())
                messages.player_won_message(money.get_win_prize())
            else:
                money.decrease_money(money.get_pull_cost())
                messages.player_lost_message(money.get_pull_cost())

            money.update_money()
            instructions.show_instructions()

        finally:
            self.processing = False

    def check_winning(self):
        """Check if all the slots have the same value so player win or lose."""
        first_slot = self.machine_slots[0]
        for slot in self.machine_slots[1:]:
            if slot.get_value() != first_slot.get_value():
                return False
        return True
