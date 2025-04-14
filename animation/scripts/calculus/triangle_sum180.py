from manim import *
from LnxScene import *
class TrianguloAngulosInternosCorrectos(Scene):
    def construct(self):

        backgroundLnx(self)
        grillado(self)

        # Configuración para líneas suaves
        config.line_stroke_width = 4
        config.line_stroke_joint_style = "round"

        scaleValue= 1.4
        radiusValue = 0.5*scaleValue/2
        radiusValueText = 1.3*radiusValue

        # Definir variables para los tamaños de fuente
        small_font_size = 25
        big_font_size = 30

        # Puntos del triángulo (equilátero para mejor visualización)
        punto_a = LEFT * scaleValue*1.2
        punto_b = RIGHT * scaleValue*0.9
        punto_c = UP *scaleValue* np.sqrt(3)/2  # Altura para equilátero

        # Líneas del triángulo
        linea_ab = Line(punto_a, punto_b, color=BLUE)
        linea_bc = Line(punto_b, punto_c, color=RED)
        linea_ca = Line(punto_c, punto_a, color=GREEN)

        linea_ba = Line(punto_b, punto_a, color=GREEN)
        linea_cb = Line(punto_c, punto_b, color=GREEN)
        linea_ac = Line(punto_a, punto_c, color=GREEN)

        # Grupo del triángulo
        triangulo = VGroup(linea_ab, linea_bc, linea_ca)

        # --- Ángulos INTERNOS (arcos hacia adentro) ---
        
        arc_alpha = Angle(linea_ab, linea_ac, radius=radiusValue, color=YELLOW)
        alpha_label = MathTex(r"\alpha", font_size=small_font_size).move_to(
            Angle(linea_ab, linea_ac, radius=radiusValueText).point_from_proportion(0.5)
        )

        # Ángulo β en B (entre AB y BC, arco hacia adentro)
        arc_beta = Angle(linea_bc, linea_ba, radius=radiusValue, color=YELLOW)
        beta_label = MathTex(r"\beta", font_size=small_font_size).move_to(
            Angle(linea_bc, linea_ba, radius=radiusValueText).point_from_proportion(0.5)
        )

        # Ángulo θ en C (entre BC y CA, arco hacia adentro)
        arc_theta = Angle(linea_ca, linea_cb, radius=radiusValue, color=YELLOW)
        theta_label = MathTex(r"\theta", font_size=small_font_size).move_to(
            Angle(linea_ca, linea_cb, radius=radiusValueText).point_from_proportion(0.5)
        )

        # Ecuación de suma de ángulos
        suma_angulos = MathTex(r"\alpha + \beta + \theta = 180^\circ", font_size=big_font_size)
        suma_angulos.next_to(triangulo, DOWN, buff=1.2)

        # ---- Animaciones ----------------
        # Dibujar triángulo
        self.play(
            LaggedStart(
                Create(linea_ab),
                Create(linea_bc),
                Create(linea_ca),
                lag_ratio=0.7
            ),
            run_time=2
        )
        self.wait(0.5)

        # Mostrar ángulos internos (arcos hacia adentro)
        self.play(
            Create(arc_alpha),
            Create(arc_beta),
            Create(arc_theta),
            FadeIn(alpha_label),
            FadeIn(beta_label),
            FadeIn(theta_label),
            run_time=1
        )
        self.wait(1)

        # Mostrar ecuación
        self.play(Write(suma_angulos))
        self.wait(1)

        # Destacar ecuación
        rect = SurroundingRectangle(suma_angulos, color=BLUE, buff=0.3)
        self.play(Create(rect))
        self.wait(3)