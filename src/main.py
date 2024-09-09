"""
This is the main module for the Slot Machine game.

It initializes the game, sets up the screen, creates the necessary objects,
and starts the main game loop.
"""


from sys import exit
from turtle import Screen, mainloop
from typing import NoReturn, TypeVar
from machine import Machine
from messages import Instructions, Messages
from money import Money
from logger import Logger
from validation import validate_configurations
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BG_COLOR,
    KEY_TO_PULL, KEY_TO_EXIT, ICON_PATH
)

# Define a type variable for Screen
ScreenType = TypeVar('ScreenType', bound=Screen)  # type: ignore


def exit_program(screen: ScreenType) -> NoReturn:
    """
    Exit the program.

    Args:
        screen (Screen): The turtle screen to close.
    """
    screen.bye()  # type: ignore
    raise SystemExit


def play(screen: ScreenType, machine: Machine) -> None:
    """
    Set up the game controls and start the game loop.

    Args:
        screen (Screen): The turtle screen for the game.
        machine (Machine): The slot machine object.
    """
    screen.listen()  # type: ignore
    screen.onkey(machine.pull, KEY_TO_PULL)  # type: ignore
    screen.onkey(lambda: exit_program(screen), KEY_TO_EXIT)  # type: ignore


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

    window = screen.getcanvas().winfo_toplevel()
    window.iconbitmap(ICON_PATH)

    screen.tracer(0)

    money = Money()
    instructions = Instructions()
    messages = Messages()
    logger = Logger()
    machine = Machine(money, instructions, messages, logger)
    screen.update()

    screen.tracer(1)
    machine.update_slots()

    logger.log("Slot Machine game is starting...")
    play(screen, machine)

    mainloop()


if __name__ == "__main__":
    main()
