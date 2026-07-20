from manim import *

class SqueezeLetter(Scene):
    def construct(self):
        # 1. Create the text object
        letter = Text("A", font_size=144)
        
        # 2. Squeeze vertically: stretch to 40% of its current height, keep width
        squeezed_letter = letter.copy()
        squeezed_letter.stretch_to_fit_height(letter.height * 0.4)
        
        # Position them on screen
        letter.shift(UP * 2)
        squeezed_letter.shift(DOWN * 2)

        self.play(Write(letter))
        self.wait(1)
        self.play(Transform(letter, squeezed_letter))
        self.wait(1)
