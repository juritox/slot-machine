from turtle import Screen, mainloop
from machine import Machine


def exit_program():
    """Exit the program."""
    screen.bye()


def play():
    """Play the slot machine game."""
    screen.listen()
    screen.onkey(machine.pull, "space")
    screen.onkey(exit_program, "Escape")


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Slot Machine")

screen.tracer(0)

machine = Machine()
screen.update()

screen.tracer(1)
machine.update_slots()

play()

mainloop()
