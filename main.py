from turtle import Screen, mainloop
from machine import Machine
from messages import Instructions, Messages
from money import Money
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BG_COLOR,
    KEY_TO_PULL, KEY_TO_EXIT
)


def exit_program(screen):
    """Exit the program."""
    screen.bye()


def play(screen, machine):
    """Play the slot machine game."""
    screen.listen()
    screen.onkey(machine.pull, KEY_TO_PULL)
    screen.onkey(lambda: exit_program(screen), KEY_TO_EXIT)


def main():
    """Initialize the slot machine game and start the main loop."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.title(SCREEN_TITLE)

    screen.tracer(0)

    money = Money()
    instructions = Instructions()
    messages = Messages()
    machine = Machine(screen, money, instructions, messages)
    screen.update()

    screen.tracer(1)
    machine.update_slots()

    play(screen, machine)

    mainloop()


if __name__ == "__main__":
    main()
