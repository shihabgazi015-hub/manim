from manim import *
from scipy.stats import chi2

class ChiSquareViz(Scene):
    def construct(self):
        # 1. Set the Statistician's Environment
        self.camera.background_color = "#06000c"
        
        # Style Constants
        MY_COLOR = "#db419b"
        AXIS_COLOR = "#DD6C6C"
        
        # 2. Define the Coordinate System
        # df=50 means Mean=50, SD=10. Range [0, 100] covers 5 sigmas.
        # Peak probability is around 0.04, so y_range=[0, 0.06] fits well.
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 0.06, 0.01],
            axis_config={"color": AXIS_COLOR, "include_tip": True},
            x_length=10,
            y_length=6,
            x_axis_config={"numbers_to_include": np.arange(0, 101, 20)}
        ).center()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("x", color=AXIS_COLOR), 
            y_label=MathTex("f(x)", color=AXIS_COLOR)
        )

        # 3. Plot the Chi-Square Distribution (df=50)
        df = 50
        curve = axes.plot(
            lambda x: chi2.pdf(x, df),
            x_range=[0, 100],
            color=MY_COLOR,
            stroke_width=4
        )

        # 4. Handle the "Area" (P-Value Visualization)
        # We calculate the critical value for a standard alpha=0.05
        critical_value = chi2.ppf(0.95, df) # approx 67.5
        
        # A. The Main Body (Light fill for context)
        main_area = axes.get_area(
            curve, 
            x_range=[0, critical_value], 
            color=MY_COLOR, 
            opacity=0.2 
        )
        
        # B. The P-Value Tail (Your requested specific 0.75 opacity)
        # This highlights the "significant" area under the curve
        p_value_area = axes.get_area(
            curve, 
            x_range=[critical_value, 100], 
            color=MY_COLOR, 
            opacity=0.75
        )

        # 5. Annotations
        # Label the degrees of freedom
        title = Tex(f"$\chi^2$ Distribution ($df={df}$)", color=WHITE)
        title.to_edge(UP)

        # Label the P-value
        p_label = Tex("p-value area ($>67.5$)", color=MY_COLOR, font_size=32)
        p_label.next_to(p_value_area, UP, buff=0.5).shift(RIGHT)
        
        p_arrow = Arrow(p_label.get_bottom(), p_value_area.get_center(), color=MY_COLOR)

        # 6. Animation Sequence
        self.play(FadeIn(axes), Write(labels))
        self.play(Create(curve), run_time=2)
        self.play(FadeIn(main_area), run_time=1)
        self.play(
            DrawBorderThenFill(p_value_area), 
            run_time=1.5
        )
        self.play(Write(title), FadeIn(p_label), GrowArrow(p_arrow))
        self.wait(3)
