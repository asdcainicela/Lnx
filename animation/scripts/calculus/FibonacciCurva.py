from manim import *
import numpy as np
from LnxScene import *

class FibonacciCurve(MovingCameraScene):
    def construct(self):
        backgroundLnx(self)
        self.frame = self.camera.frame
        def Fibonacci(n):
            if n < 0:
                print("Incorrect input")
            elif n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                return Fibonacci(n - 1) + Fibonacci(n - 2)

        lastSquare = Square(1)
        arc = ArcBetweenPoints(lastSquare.get_vertices()[2], lastSquare.get_vertices()[0])
        tex = Tex("1", font_size=20).move_to(lastSquare.get_center())
        squares = VGroup(lastSquare)

        directions = [UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT,
                      UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT,
                      UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT, UP, LEFT, DOWN, RIGHT]

        value = ValueTracker(0)
        rate = 15
        value.add_updater(lambda v: v.set_value(v.get_value() + rate))
        self.frame.add_updater(lambda v: v.set_height(squares.height * 1.2))
        self.play(Create(lastSquare), Create(arc), Create(tex))
        for i in range(2, 21):
            direction = directions[i - 2]
            square = Square(Fibonacci(i)).next_to(squares, direction, buff=00)
            squares.add(square)
            self.play(Create(square, run_time=0.5), Create(
                MathTex(f"{Fibonacci(i)}", font_size=square.side_length * 20).move_to(square.get_center())))
            self.play(self.frame.animate.move_to(squares.get_center()), run_time=0.2)
            if direction is UP:
                arc = ArcBetweenPoints(square.get_vertices()[3], square.get_vertices()[1])
                squares.add(arc)
                self.play(Create(arc))
            if direction is LEFT:
                arc = ArcBetweenPoints(square.get_vertices()[0], square.get_vertices()[2])
                squares.add(arc)
                self.play(Create(arc))
            if direction is DOWN:
                arc = ArcBetweenPoints(square.get_vertices()[1], square.get_vertices()[3])
                squares.add(arc)
                self.play(Create(arc))
            if direction is RIGHT:
                arc = ArcBetweenPoints(square.get_vertices()[2], square.get_vertices()[0])
                squares.add(arc)
                self.play(Create(arc))
            if 10 <= i < 20:
                self.play(squares.animate.set_stroke(width=squares.get_stroke_width() + 20))
            elif i >= 20:
                self.play(squares.animate.set_stroke(width=squares.get_stroke_width() + 300))

        self.wait(6)
        self.frame.clear_updaters()
        self.play(self.frame.animate.move_to(lastSquare.get_center()))
        self.play(self.frame.animate.set_height(lastSquare.get_height() * 5), squares.animate.set_stroke(width=10), run_time=3.5)
        self.wait(2)


#with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
 #   scene = FibonacciCurve()
  #  scene.render()
