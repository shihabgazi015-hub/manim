# from manim import *

# class SingleWordStandardDeviation(Scene):
#     def construct(self):
#         # 1. Background Setup (White)
#         self.camera.background_color = WHITE
        
#         # 2. Define Custom Color and Font Size
#         MY_PURPLE = "#572A74"
#         WORD_SIZE = 144  # This makes the single word "Big"

#         # 3. Create a list of the words in the sentence
#         full_sentence = "The standard deviation is a measure that indicates how much data is scattered around the mean."
#         words_list = full_sentence.split() # Splitting the string into a list

#         # 4. Display the FIRST word
#         # Create the first Text object manually to start the sequence
#         first_word = words_list[0]
#         current_mobject = Text(first_word, color=MY_PURPLE, font_size=WORD_SIZE)
        
#         self.play(Write(current_mobject))
#         self.wait(0.4) # Short pause to read the first word

#         # 5. Animation Loop (Start from the 2nd word to the end)
#         # We loop through the list starting at index 1 [1:]
#         for next_word_string in words_list[1:]:
            
#             # a. Create the NEXT word object (centered by default)
#             next_mobject = Text(next_word_string, color=MY_PURPLE, font_size=WORD_SIZE)
            
#             # b. ReplacementTransform: The smooth transition
#             # This makes current_mobject morph into next_mobject
#             self.play(ReplacementTransform(current_mobject, next_mobject), run_time=0.6)
            
#             # c. Update which word is "current"
#             # next_mobject is now on screen, so we save it as 'current_mobject' for the next loop iteration
#             current_mobject = next_mobject
            
#             # d. Short pause between words
#             self.wait(0.3)

#         # 6. Final Wait and Fade Out
#         # At this point, current_mobject holds the final word "mean."
#         self.wait(1.5)
#         self.play(FadeOut(current_mobject))




# 2

# from manim import *

# class FormulasScene(Scene):
#     def construct(self):
#         # 1. Setup
#         self.camera.background_color = WHITE
#         MY_PURPLE = "#572A74"
        
#         # 2. Part 1: The Sentence (One word at a time)
#         intro_text = "And the formulas are"
#         words = intro_text.split()
        
#         current_word = Text(words[0], color=MY_PURPLE, font_size=100)
#         self.play(Write(current_word))
#         self.wait(0.3)
        
#         for next_w in words[1:]:
#             next_obj = Text(next_w, color=MY_PURPLE, font_size=100)
#             self.play(ReplacementTransform(current_word, next_obj), run_time=0.5)
#             current_word = next_obj
#             self.wait(0.3)
            
#         self.play(FadeOut(current_word))
#         self.wait(0.5)

#         # 3. Part 2: The Formulas
#         # Use MathTex for LaTeX formatting. 
#         # 'r' before the string handles backslashes correctly in Python.
        
#         pop_label = Text("Population", color=MY_PURPLE, font_size=36)
#         pop_formula = MathTex(
#             r"\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}", 
#             color=MY_PURPLE, font_size=60
#         )
        
#         sample_label = Text("Sample", color=MY_PURPLE, font_size=36)
#         sample_formula = MathTex(
#             r"s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}", 
#             color=MY_PURPLE, font_size=60
#         )

        # 4. Positioning
        # Group label and formula together
        # pop_group = VGroup(pop_label, pop_formula).arrange(DOWN, buff=0.5)
        # sample_group = VGroup(sample_label, sample_formula).arrange(DOWN, buff=0.5)
        
        # # Put them side by side
        # both_formulas = VGroup(pop_group, sample_group).arrange(RIGHT, buff=2)
        
        # # 5. Animation
        # self.play(Write(both_formulas))
        # self.wait(3)



# 3

# from manim import *

# class ShowImage(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
        
#         # 1. Load the image
#         # Replace "my_photo.png" with your actual file name
#         img = ImageMobject("me.jpeg")
        
#         # 2. Adjust size and position
#         img.scale(.5) # Make it smaller
#         img.to_edge(UP) # Move it to the top
        
#         # 3. Animate it onto the screen
#         # Note: ImageMobjects use FadeIn/FadeOut or MoveInFromEdge 
#         # because they don't have "outlines" like shapes do.
#         self.play(FadeIn(img))
#         self.wait(2)
        
#         # You can shake it or do other animations if you like
#         self.play(img.animate.shift(LEFT*0.5), run_time=0.5)
#         self.play(img.animate.shift(RIGHT*0.5), run_time=0.5)
#         self.play(img.animate.shift(LEFT*0.5), run_time=0.5)
#         self.play(img.animate.shift(RIGHT*0.5), run_time=0.5)
#         self.wait(1)

#4
# from manim import *

# class MathEquation(Scene):
#     def construct(self):
#         # 1. Setup
#         self.camera.background_color = WHITE
#         MY_PURPLE = "#572A74"
#         TEXT_SIZE = 144 # Big font size as before

#         # 2. Define the parts of the equation
#         # We split them so we can transform them one by one
#         parts = ["-10", "+", "0", "+", "10", "=", "0"]
        
#         # 3. Create the first object
#         current_obj = Text(parts[0], color=MY_PURPLE, font_size=TEXT_SIZE)
        
#         # 4. Animation Sequence
#         self.play(Write(current_obj))
#         self.wait(0.4)

#         for next_part in parts[1:]:
#             # # Create the next piece of the equation
#             # next_obj = Text(next_part, color=MY_PURPLE, font_size=TEXT_SIZE)
#             # Alternative inside the loop if using MathTex:
#             next_obj = MathTex(next_part, color=MY_PURPLE, font_size=TEXT_SIZE)
            
#             # Use FadeTransform to morph the old part into the new part
#             self.play(
#                 FadeTransform(current_obj, next_obj), 
#                 run_time=0.6
#             )
            
#             # Update the reference for the next loop
#             current_obj = next_obj
#             self.wait(0.3)

#         # 5. Final pause
#         self.wait(2)
#         self.play(FadeOut(current_obj))

#5
#




from manim import *

class SubtractionSequence(Scene):
    def construct(self):
        # 1. Setup Background
        self.camera.background_color = BLACK
        MY_PURPLE = "#572A74"
        TEXT_SIZE = 144 

        # 2. Define the equations as a list of strings
        # Using spaces to keep the "=" and numbers aligned
        equations = [
            "70 - 80 = -10",
            "80 - 80 =  00",
            "90 - 80 =  10"
        ]

        # 3. Create the first equation object
        current_eq = Text(equations[0], color=MY_PURPLE, font_size=TEXT_SIZE, font="Consolas")
        
        # 4. Initial Animation
        self.play(Write(current_eq))
        self.wait(1.5)

        # 5. Loop through the remaining equations
        for next_text in equations[1:]:
            # Create the next equation
            # 'font="Consolas"' ensures numbers align perfectly (monospaced)
            next_eq = Text(next_text, color=MY_PURPLE, font_size=TEXT_SIZE, font="Consolas")
            
            # Smoothly transform the old equation into the new one
            self.play(
                ReplacementTransform(current_eq, next_eq),
                run_time=0.8
            )
            
            # Update the reference and pause
            current_eq = next_eq
            self.wait(1.5)

        # 6. Final Outro
        self.play(FadeOut(current_eq))
        self.wait(1)