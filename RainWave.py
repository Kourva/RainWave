# Rainbow wave
# Github: https://github.com/kozyol

# Imports
import math
import turtle
import random

# Main class
class Wave:
    """Returns a window with your wave

    Usage: Wave(bgcolor, fgcolor, pensize, repeat, speed, step)

      * bgcolor: Background color (defaults to Black)
      * fgcolor: Forground color (defaults to White)
      * pensize: Pen size (defaults to 2)
      * repeat: Repeat times (defaults to 10)
      * speed: Draw speed (defaults to 5)
      * step: Wave steps - from 0 to 4400 with step (defaults to 10)
    """

    # initializing
    def __init__(
        self, bgcolor="Black", fgcolor="white", pensize=2, repeat=10, speed=5, step=10
    ):
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.pensize = pensize
        self.repeat = repeat
        self.speed = speed
        self.step = step

    # Length
    def __len__(self):
        return self.repeat

    # Color generator
    def color_generator(self):
        """Color generator for rainbow wave"""

        color_keys = "1234567890abcdef"
        return "#" + "".join(random.choices(color_keys, k=6))

    # Main function
    def run(self):
        """Run method to display window with your wave"""

        window = turtle.Screen()
        window.bgcolor(self.bgcolor)

        # coordinate setting
        window.setworldcoordinates(0, -3, 4400, 3)
        window.title("Rainbow Wave")
        root = turtle.Turtle()

        for i in range(self.repeat):

            root.hideturtle()
            root.color("black")

            # Draw a vertical line
            root.speed(self.speed)
            root.goto(0, 3)
            root.clear()

            root.color(self.fgcolor)
            # Label
            root.goto(0, 2.8)
            root.write(
                f"\t\t\t\t\t\t\t speed {self.speed} | step {self.step} | repeat {self.repeat}\t\tCurrent step: {i+1}",
                align="center",
            )

            root.goto(0, -3)
            root.goto(0, 0)

            # Draw a Horizontal line
            root.goto(4400, 0)
            root.penup()
            root.goto(0, 0)
            root.pendown()
            root.pensize(1)

            count = 0
            # Generate wave form
            for x in range(0, 4400, self.step):
                y = math.sin(math.radians(x))
                if count == 4:
                    root.pencolor(self.color_generator())
                    count = 0
                root.goto(x, y + random.randrange(-1, 2))
                count += 1
