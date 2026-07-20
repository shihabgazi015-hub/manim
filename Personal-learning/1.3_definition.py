from tkinter import Text
from manim import *

class StandardDeviationDefinition(Scene):
    def construct(self):
        # Set the scene background color to white
        self.camera.background_color = WHITE

        line = Line(start=LEFT, end=RIGHT, color=GREEN, stroke_width=2) 
        # Create the text object
        # The color is set using the hex code provided (#572A74)
        definition_text = Text("-10\n+0\n+10\n=0",color=GREEN,font_size=60, font="Math")# Optionally set the font size for clarity, e.g., 36 or default 48        )

        definition_text.to_edge(UP)  # Move the text to the top edge

        # Group and arrange the text for better visibility if needed, or keep it as one block for simple fade-in.
        # Given it's a short text, keeping it as a single object is best.
        
        # Display the animation
        # Use Write to animate it typing out, or FadeIn for a gentle appearance.
        # A simple Write effect is good for educational texts.
        self.play(Write(definition_text, run_time=5))
        self.play(Create(line))
        
        # Wait for a few seconds so the user can read the full text
        self.wait(5)

        # Optionally FadeOut at the end (useful if chaining multiple scene clips together)
        self.play(FadeOut(definition_text))
        self.wait(1)