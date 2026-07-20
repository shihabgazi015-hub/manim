from manim import *

class VerticalMath(Scene):
    def construct(self):
        # 1. Setup Background
        self.camera.background_color = WHITE
        MY_PURPLE = "#572A74"

        # 2. Create the text block
        # We use a raw string (r"...") and triple quotes for multi-line text
        # I added some spaces to help align the numbers over each other
        equation_text = Text(
            "70 - 80= -10", 
            color=MY_PURPLE,
            font_size=75, # 360 is massive; 144 is usually better for 4K
            line_spacing=0.8 # Brings the lines slightly closer together
        )

        # 3. Positioning
        # .move_to(ORIGIN) is the same as .to_center() but more standard in Manim
        equation_text.move_to(ORIGIN)

        # 4. Animation
        # 'Write' will draw the characters one by one
        self.play(Write(equation_text), run_time=4)
        
        self.wait(3)

        # 5. Outro
        self.play(FadeOut(equation_text))
        self.wait(1)