from turtle import Screen, mainloop
from machine import Machine
from messages import Instructions, Messages
from money import Money


def exit_program(screen):
    """Exit the program."""
    screen.bye()


def play(screen, machine):
    """Play the slot machine game."""
    screen.listen()
    screen.onkey(machine.pull, "space")
    screen.onkey(lambda: exit_program(screen), "Escape")


def main():
    """Initialize the slot machine game and start the main loop."""
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Slot Machine")

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
