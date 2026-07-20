from manim import *

class ShapeMorph(Scene):
    def construct(self):
        # Define all shapes
        circle = Circle(radius=2, color=RED, fill_opacity=1)
        rectangle = Rectangle(width=4, height=4, color=BLUE, fill_opacity=0.75)
        triangle = Triangle().set_fill(RED, opacity=1).set_stroke(BLUE, width=4)

        # 1. Show the circle
        self.play(Create(circle))
        self.wait(2)
        
        # 2. Transform circle into rectangle
        self.play(ReplacementTransform(circle, rectangle))
        self.wait(2)
        
        # 3. Transform rectangle into triangle
        self.play(ReplacementTransform(rectangle, triangle))
        self.wait(2)
