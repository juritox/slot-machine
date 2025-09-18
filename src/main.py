"""
This is the main module for the Slot Machine game.

It initializes the game, sets up the screen, creates the necessary objects,
and starts the main game loop.
"""

import sys
from pathlib import Path
from tkinter import PhotoImage
from turtle import Screen, mainloop
from typing import Protocol, Callable, Any, NoReturn
from machine import Machine
from messages import Instructions, Messages
from money import Money
from logger import Logger
from validation import validate_configurations
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BG_COLOR,
    KEY_TO_PULL, KEY_TO_EXIT, ICON_FILE_PNG, ICON_FILE_ICO
)


class ScreenProtocol(Protocol):
    """
    Protocol defining the methods used from turtle.Screen in the slot machine game.

    Used for type checking purposes.
    """

    def bye(self) -> None:
        """Close the turtle screen."""
        ...

    def listen(self) -> None:
        """Start listening for events."""
        ...

    def onkey(self, fun: Callable[[], None], key: str) -> None:
        """Bind a function to a key press event."""
        ...

    def setup(self, width: int | float, height: int | float) -> None:
        """Set the screen size."""
        ...

    def bgcolor(self, color: str) -> None:
        """Set the background color of the screen."""
        ...

    def title(self, titlestring: str) -> None:
        """Set the window title."""
        ...

    def tracer(self, n: int) -> None:
        """Control animation tracer delay."""
        ...

    def update(self) -> None:
        """Update the screen manually."""
        ...

    def getcanvas(self) -> Any:
        """Get the underlying Tkinter canvas widget."""
        ...


def exit_program(screen: ScreenProtocol) -> NoReturn:
    """
    Exit the program.

    Args:
        screen (ScreenProtocol): The turtle screen to close.
    """
    screen.bye()
    sys.exit()


def play(screen: ScreenProtocol, machine: Machine) -> None:
    """
    Set up the game controls and start the game loop.

    Args:
        screen (ScreenProtocol): The turtle screen for the game.
        machine (Machine): The slot machine object.
    """
    screen.listen()
    screen.onkey(machine.pull, KEY_TO_PULL)
    screen.onkey(lambda: exit_program(screen), KEY_TO_EXIT)


def set_icon(screen: ScreenProtocol) -> None:
    """
    Set the application window icon in a cross-platform manner using Tkinter.

    Uses a ".ico" file for Windows and a ".png" file for other platforms.
    Obtains the underlying Tkinter root window from the given screen object
    to apply the icon accordingly.

    Args:
        screen (ScreenProtocol): The screen object providing access to the Tkinter root window.
    """
    root = screen.getcanvas().winfo_toplevel()

    # Use pathlib to determine the correct path
    base_path = Path(__file__).parent
    icons_path = base_path.parent / "assets" / "icons"

    if sys.platform == "win32":
        # For Windows
        icon_path = icons_path / ICON_FILE_ICO
        root.iconbitmap(default=str(icon_path))
    else:
        # For Linux and other platforms
        icon_path = icons_path / ICON_FILE_PNG
        icon = PhotoImage(file=str(icon_path))
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
