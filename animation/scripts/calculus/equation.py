from manim import *


class LinearEquation(Scene):
    def construct(self):
        self.camera.background_color = "#111317" 
        expr = MathTex(r" \frac{2x+5}{3} = 7 ", font_size=50).shift(UP * 0.5)

        question = Tex("Solve for $x$", font_size=50).next_to(expr, DOWN, buff=1)

        self.wait(1) 
        self.play(Write(expr))
        self.play(Write(question))
        self.wait(15)


 