from manim import *

class TrianguloConLineas(Scene):
    def construct(self):
        # Definir los puntos del triángulo
        punto_a = LEFT * 2
        punto_b = RIGHT * 2
        punto_c = UP * 2

        # Crear las tres líneas
        linea_ab = Line(punto_a, punto_b, color=BLUE)
        linea_bc = Line(punto_b, punto_c, color=RED)
        linea_ca = Line(punto_c, punto_a, color=GREEN)

        # Agrupar las líneas para formar el triángulo
        triangulo = VGroup(linea_ab, linea_bc, linea_ca)

        # Mostrar el triángulo en la escena
        self.play(Create(linea_ab), Create(linea_bc), Create(linea_ca))
        self.wait(2)

        # También puedes animar el triángulo como un grupo
        self.play(triangulo.animate.shift(DOWN))
        self.wait(1)