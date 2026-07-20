from manim import *

class RedCircle(Scene):
    def construct(self):
        # Create a circle, set fill to red, and make it fully opaque
        circle = Circle(radius=2, color=RED, fill_opacity=1)
        rectangle = Rectangle(width=4, height=4, color=BLUE, fill_opacity=0.75)
        # Solid red inside, blue border with a width of 4
        triangle = Triangle().set_fill(RED, opacity=1).set_stroke(BLUE, width=4)

        self.play(Create(circle))
        self.wait(2)
        self.play(Transform(circle, rectangle))
        self.wait(2)
        self.play(Transform(rectangle, triangle))
        self.wait(2)
