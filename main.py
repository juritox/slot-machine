"""
This is the main module for the Slot Machine game.

It initializes the game, sets up the screen, creates the necessary objects,
and starts the main game loop.
"""

from turtle import Screen, mainloop
from typing import NoReturn
from machine import Machine
from messages import Instructions, Messages
from money import Money
from validation import validate_configurations
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BG_COLOR,
    KEY_TO_PULL, KEY_TO_EXIT
)


def exit_program(screen: Screen) -> NoReturn:
    """
    Exit the program.

    Args:
        screen (Screen): The turtle screen to close.
    """
    screen.bye()


def play(screen: Screen, machine: Machine) -> None:
    """
    Set up the game controls and start the game loop.

    Args:
        screen (Screen): The turtle screen for the game.
        machine (Machine): The slot machine object.
    """
    screen.listen()
    screen.onkey(machine.pull, KEY_TO_PULL)
    screen.onkey(lambda: exit_program(screen), KEY_TO_EXIT)


def main() -> None:
    """
    Initialize the slot machine game and start the main loop.

    This function sets up the game environment, creates necessary objects,
    and starts the game loop.
    """
    try:
        validate_configurations()
    except ValueError as e:
        print(f"Configuration Error:\n{e}")
        exit(1)  # Terminate the program immediately

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.title(SCREEN_TITLE)

    screen.tracer(0)

    money = Money()
    instructions = Instructions()
    messages = Messages()
    machine = Machine(money, instructions, messages)
    screen.update()

    screen.tracer(1)
    machine.update_slots()

    play(screen, machine)

    mainloop()


if __name__ == "__main__":
    main()
