from manim import *

class demo(Scene):
    def construct(self):
        t1 = Text("SGS", font_size=85, color=BLUE)
        t2 = Text("Shihab Gazi SUSTian", font_size=85, color=RED)
        self.play(Write(t1))
        self.wait(0.5)

        # self.play(Transform(t1, t2))
        self.play(ReplacementTransform(t1[0], t2[:6]), run_time=0.75)
        self.wait(0.2)
        self.play(ReplacementTransform(t1[1], t2[6:10]), t1[2].animate.shift(RIGHT*.65), run_time=0.75)
        self.wait(0.2)
        self.play(ReplacementTransform(t1[2], t2[10:]), run_time=0.75)
        self.wait(0.2)

        self.play(t2[6:10].animate.shift(UP * 0.65), run_time=0.75, rate_func=there_and_back_with_pause)

        self.wait(3)