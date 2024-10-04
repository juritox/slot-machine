"""
This is the main module for the Slot Machine game.

It initializes the game, sets up the screen, creates the necessary objects,
and starts the main game loop.
"""

import sys
import os
from tkinter import PhotoImage
from turtle import Screen, mainloop
from typing import TypeAlias, NoReturn
from machine import Machine
from messages import Instructions, Messages
from money import Money
from logger import Logger
from validation import validate_configurations
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BG_COLOR,
    KEY_TO_PULL, KEY_TO_EXIT, ICON_FILE_PNG, ICON_FILE_ICO
)

# Define a type alias for Screen
ScreenType: TypeAlias = Screen  # type: ignore


def exit_program(screen: ScreenType) -> NoReturn:
    """
    Exit the program.

    Args:
        screen (Screen): The turtle screen to close.
    """
    screen.bye()  # type: ignore
    sys.exit()


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


def set_icon(screen):
    """
    Set the application icon in a cross-platform manner.
    """
    root = screen.getcanvas().winfo_toplevel()

    # Determine the correct path whether running as .py or .pyw
    base_path = os.path.dirname(os.path.abspath(__file__))
    icons_path = os.path.join(base_path, "..", "assets", "icons")

    if sys.platform == "win32":
        # For Windows
        icon_path = os.path.join(icons_path, ICON_FILE_ICO)
        root.iconbitmap(default=icon_path)
    else:
        # For Linux and other platforms
        icon_path = os.path.join(icons_path, ICON_FILE_PNG)
        icon = PhotoImage(file=icon_path)
        root.iconphoto(True, icon)


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
        sys.exit(1)  # Terminate the program immediately

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.title(SCREEN_TITLE)

    set_icon(screen)

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
