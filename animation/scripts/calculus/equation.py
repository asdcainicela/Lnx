from manim import *


class LinearEquation(Scene):
    def construct(self):
        self.camera.background_color = "#111317" 
        expr = MathTex(r" \frac{2x+5}{3} = 7 ", font_size=55).shift(UP * 0.5)

        question = MathTex(r"x=?", font_size=50).next_to(expr, DOWN, buff=1) 
        texts = VGroup(question).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(Write(expr))
        self.wait(1) 
        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(question),
                Wait(1.0),
                # ...or multiple Mobjects at once! 
            ),
        ) 
        self.wait(2)  


 