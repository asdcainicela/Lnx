from manim import *
import numpy as np
from LnxScene import *

class FibonacciCurve(MovingCameraScene):
    def construct(self):
        # Setup background and camera frame
        backgroundLnx(self)
        frame = self.camera.frame

        # Recursive Fibonacci function
        def Fibonacci(n):
            if n < 0:
                print("Incorrect input")
            elif n in (0, 1, 2):
                return 1 if n else 0
            return Fibonacci(n - 1) + Fibonacci(n - 2)

        # Initial square and arc
        last_square = Square(1)
        arc = ArcBetweenPoints(
            last_square.get_vertices()[2],
            last_square.get_vertices()[0]
        )
        tex = Tex("1", font_size=20).move_to(last_square.get_center())
        squares = VGroup(last_square)

        # Directions for placing new squares
        directions = [UP, LEFT, DOWN, RIGHT] * 12  # repeated pattern

        # Scale factor for text and sizes
        scale_val = 0.5

        # Camera updater: maintain a bit of margin around the group
        frame.add_updater(lambda f: f.set(width=squares.width * 1.2))

        # Draw the first square and arc
        self.play(Create(last_square), Create(arc), Create(tex))

        # Build Fibonacci squares and arcs
        for i in range(2, 5): #21
            direction = directions[i - 2]
            side = Fibonacci(i)
            square = Square(side).next_to(squares, direction, buff=0)
            squares.add(square)

            # Create square and label
            label = MathTex(f"{side}", font_size=square.side_length * 20 * scale_val)
            label.move_to(square.get_center())
            self.play(
                Create(square, run_time=0.5),
                Create(label, run_time=0.5)
            )

            # Smooth camera pan & zoom to fit new group
            self.play(
                frame.animate
                     .move_to(squares.get_center())
                     .set(width=squares.width * 1.2),
                run_time=0.5,
                rate_func=smooth
            )

            # Draw the connecting arc
            verts = square.get_vertices()
            if direction is UP:
                arc = ArcBetweenPoints(verts[3], verts[1])
            elif direction is LEFT:
                arc = ArcBetweenPoints(verts[0], verts[2])
            elif direction is DOWN:
                arc = ArcBetweenPoints(verts[1], verts[3])
            else:  # RIGHT
                arc = ArcBetweenPoints(verts[2], verts[0])
            squares.add(arc)
            self.play(Create(arc, run_time=0.3))

            # Moderate stroke growth to avoid abrupt zoom illusion
            if 10 <= i < 20:
                self.play(
                    squares.animate.set_stroke(
                        width=squares.get_stroke_width() + 5
                    ),
                    run_time=0.3
                )
            elif i >= 20:
                self.play(
                    squares.animate.set_stroke(
                        width=squares.get_stroke_width() + 15
                    ),
                    run_time=0.3
                )

        # Pause, then reset camera to focus back on the first square
        self.wait(2)
        frame.clear_updaters()
        self.play(
            frame.animate
                 .move_to(last_square.get_center())
                 .set(width=last_square.width * 1.5),
            squares.animate.set_stroke(width=10),
            run_time=3
        )
        self.wait(2)
