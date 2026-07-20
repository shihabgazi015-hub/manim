from manim import *
from statanim.distributions.normal3d import NormalCurve3D
from statanim.probability.tree import ProbabilityTree3D
from statanim.core.colors import DARK_THEME

class BernoulliToBetaTransition(Scene):
    def construct(self):
        # Initialize standard 2D axes for probability rendering
        axes = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 4, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_numbers": True, "color": BLUE}
        )
        self.play(Create(axes))
        self.wait(1)

        # Draw the physical balance beam representing the Bernoulli PMF
        beam = Line(
            start=axes.c2p(0, 0.1, 0),
            end=axes.c2p(1, 0.1, 0),
            color=GRAY,
            stroke_width=8
        )
        self.play(Create(beam))

        # Model point masses representing Bernoulli probabilities (p = 0.4)
        p_init = 0.4
        mass_0 = Dot(point=axes.c2p(0, 0.1, 0), radius=0.2 * (1.0 - p_init), color=RED)
        mass_1 = Dot(point=axes.c2p(1, 0.1, 0), radius=0.2 * p_init, color=GREEN)
        
        lbl_0 = Tex(r"1 - p = 0.6").next_to(mass_0, UP)
        lbl_1 = Tex(r"p = 0.4").next_to(mass_1, UP)

        self.play(
            FadeIn(mass_0), FadeIn(mass_1),
            Write(lbl_0), Write(lbl_1)
        )
        self.wait(1)

        # Position the pivot point at the center of gravity (Mean)
        pivot = Triangle(color=YELLOW).scale(0.2)
        pivot.move_to(axes.c2p(p_init, 0.0, 0))
        lbl_pivot = Tex(r"E[X] = p", color=YELLOW).next_to(pivot, DOWN)

        self.play(Create(pivot), Write(lbl_pivot))
        self.wait(1.5)

        # Warp the discrete PMF masses into a continuous Beta prior (alpha = 2, gamma = 3)
        # Beta prior PDF: f(p) = 12 * p * (1-p)^2
        beta_prior_curve = axes.plot(
            lambda x: 12.0 * x * ((1.0 - x) ** 2.0) if 0 <= x <= 1 else 0,
            color=YELLOW,
            use_smoothing=True
        )
        lbl_beta = Tex(r"\operatorname{Beta}(p; 2, 3)", color=YELLOW).to_corner(UP + RIGHT)

        self.play(
            FadeOut(mass_0), FadeOut(mass_1),
            FadeOut(lbl_0), FadeOut(lbl_1),
            FadeOut(beam),
            Transform(pivot, beta_prior_curve),
            Transform(lbl_pivot, lbl_beta),
            run_time=2.5
        )
        self.wait(2)