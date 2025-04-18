from manim import *

class ParabolaExample(Scene):
    def construct(self):
        # Configuración de la escena
        axes = Axes(x_range=[0, 5], y_range=[0, 4])
        graph = axes.plot_parametric_curve(
            lambda t: np.array([t, 2*t - 0.5*t**2, 0]),
            t_range=[0, 4],
            color=BLUE
        )
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        self.add(axes, dot)
        
        # Animación
        self.play(MoveAlongPath(dot, graph, rate_func=linear, run_time=3))
        self.wait()