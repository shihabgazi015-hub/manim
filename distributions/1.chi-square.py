from manim import *
import numpy as np
from scipy.stats import chi2

class ChiSquarePlot(Scene):
    def construct(self):
        # 1. Create the coordinate axes
        axes = Axes(
            x_range=[0, 15, 2],       # [min, max, step]
            y_range=[0, 0.5, 0.1],
            axis_config={"include_tip": True, "stroke_color": GREY},
            x_length=9,
            y_length=5
        ).to_edge(DOWN, buff=0.5)

        # Add labels to the axes
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # 2. Define the Chi-Square curve using SciPy (Degrees of Freedom = 4)
        df = 4
        chi2_curve = axes.plot(
            lambda x: chi2.pdf(x, df),
            x_range=[0.01, 14],       # Start slightly above 0 to avoid computational boundaries
            color="#FF5733",          # Your custom stroke color
            stroke_width=5            # Custom stroke width
        )

        # 3. Add a label for the distribution
        curve_label = MathTex(r"\chi^2 \text{ distribution (df=4)}", color="#FF5733")
        curve_label.next_to(chi2_curve, UR, buff=0.1).scale(0.8)

        # 4. Animate the drawing process
        self.play(Create(axes), Write(labels))
        self.play(Create(chi2_curve), Write(curve_label), run_time=2)
        self.wait(2)
