from manim import *

class ShapeMorphWithDetails(Scene):
    def construct(self):
        # 1. Define Shapes
        circle = Circle(radius=2, color=RED, fill_opacity=1)
        rectangle = Rectangle(width=4, height=4, color=BLUE, fill_opacity=0.75)
        
        # Base triangle modified to custom width and height
        triangle = Triangle().set_fill(RED, opacity=1).set_stroke(BLUE, width=4)
        triangle.stretch_to_fit_width(5)
        triangle.stretch_to_fit_height(3)

        # 2. Define Text Labels
        circle_label = Text("Circle", font_size=36).next_to(circle, UP)
        rect_label = Text("Rectangle", font_size=36).next_to(rectangle, UP)
        tri_label = Text("Triangle", font_size=36).next_to(triangle, UP)

        # 3. Animation Sequence with Easing and Labels
        
        # Step 1: Show Circle and its label
        self.play(Create(circle), Write(circle_label), run_time=1.5, rate_func=linear) # Constant speed
        self.wait(1.5)
        
        # Step 2: Morph to Rectangle with standard ease-in-out
        self.play(ReplacementTransform(circle, rectangle),ReplacementTransform(circle_label, rect_label),run_time=2,rate_func=linear) # Constant speed transformation
        self.wait(1.5)
        
        # Step 3: Morph to Triangle with sudden acceleration (Ease In)
        self.play(ReplacementTransform(rectangle, triangle),ReplacementTransform(rect_label, tri_label),run_time=1,rate_func=ease_in_quad)
        self.wait(1.5)