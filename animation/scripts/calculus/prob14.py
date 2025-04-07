from manim import *
from LnxScene import backgroundLnx, BoxAnimation, SmartMathTex, MathPazoKpTemplate

# Clase principal de animación
class CompleteAnimation(Scene):
    def construct(self):
        # Fondo personalizado (probablemente con color o imagen)
        backgroundLnx(self)

        # Establecer el template LaTeX con fuentes elegantes (mathpazo + kpfonts)
        self.camera.tex_template = MathPazoKpTemplate()

        # Crear la caja animada con imagen y borde dorado
        box_anim = BoxAnimation(
            self,
            width=4.2,
            height=2.5,
            image_path="logo.png",  # Imagen del logo en la esquina inferior izquierda
            box_stroke_color=GOLD,
        )
        box_anim.on()  # Mostrar caja y activar animaciones iniciales

        # Parámetros útiles para ajustar el contenido dentro de la caja
        box = box_anim.box
        content_width = box.width * 0.9
        content_height = box.height * 0.7

        # TEXTO: Enunciado del problema
        texto1 = MathTex( 
            r"\text{Calcule la integral:} ",
            font_size=22
        )

        # ECUACIÓN: Integral principal
        ecuacion = SmartMathTex(
            r"\int_{1}^{\infty} \frac{x^{\alpha} \ln^{b}(x)}{1 + x + x^2 + \dots + x^n} \, \mathrm{d}x",
            target_width=content_width,  # Escalar para que encaje dentro de la caja
            target_height=content_height * 0.6,
            font_size=25
        )

        # TEXTO: Condiciones de la integral
        texto2 = MathTex( 
            r"\text{donde } b \geq 0,\ n \in \mathbb{Z}^+,\ \alpha < n - 1",
            font_size=16
        )

        # Agrupar y alinear los elementos de arriba a abajo (centrados en la caja)
        grupo = VGroup(texto1, ecuacion, texto2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        grupo.move_to(box.get_center())

        # ANIMACIONES de entrada: Escritura tipo "dibujado"
        self.play(Write(texto1))  # Escribir el enunciado
        self.wait(0.5)

        self.play(Write(ecuacion))  # Escribir la integral
        self.wait(0.5)

        self.play(Write(texto2))  # Escribir las condiciones
        self.wait(1)

        # Tiempo extra para que el espectador lea con calma
        self.wait(3)

        # SOLUCIÓN: etiqueta en la parte superior de la pantalla
        solucion_label = Text("  Solución  ", font_size=16, color=WHITE)
        fondoTextSolution = BackgroundRectangle(solucion_label, color=BLACK, fill_opacity=1)
        grupo2 = VGroup(fondoTextSolution, solucion_label).to_edge(UP)

        # TRANSICIÓN: Remover problema y mostrar "Solución"
        self.play(
            ReplacementTransform(grupo, grupo2, run_time=1),  # Cambiar el grupo de texto por la etiqueta "Solución"
            FadeOut(box_anim.box),                            # Desaparecer la caja
            FadeOut(box_anim.fill),                           # Desaparecer fondo de la caja
            box_anim.imagen.animate.scale(0.3).to_corner(DL), # Mover y escalar imagen a la esquina inferior izquierda
            run_time=1
        )

        # Pausa final
        self.wait(2)
        # solucion aqui dbemos escribir, todo lo de arriba siempre se va a repetir lo mismo

        #--------------------#


class IntegralEquations(Scene):
    def construct(self): 
        # Establecer el fondo
        backgroundLnx(self)
        
        # Establecer el template LaTeX con fuentes elegantes (mathpazo + kpfonts)
        self.camera.tex_template = MathPazoKpTemplate()
        
        # Definición de la integral general
        texto1 = MathTex(
            r"\text{Definición de la integral general:}",
            font_size=16
        )

        solEq1 = MathTex(
            r"I(\alpha, b, n) = \int_{1}^{\infty} \frac{x^{\alpha} \ln^{b}(x)}{1 + x + x^2 + \dots + x^n} \, \mathrm{d}x",
            font_size=16
        )

        # Caso cuando b=0
        texto2 = MathTex(
            r"\text{Caso cuando } b=0:",
            font_size=16
        )

        solEq2 = MathTex(
            r"I(\alpha, 0, n) = \int_{1}^{\infty} \frac{x^{\alpha}}{1 + x + x^2 + \cdots + x^n} \, \mathrm{d}x",
            font_size=16
        )

        # Serie geométrica en el denominador
        texto3 = MathTex(
            r"\text{El denominador es una serie geométrica:}",
            font_size=16
        )

        solEq3 = MathTex(
            r"1 + x + \cdots + x^n = \frac{1 - x^{n+1}}{1 - x}, \quad \text{para } x \neq 1",
            font_size=16
        )

        # Reemplazo de la serie geométrica
        texto4 = MathTex(
            r"\text{Reemplazando en } I(\alpha, 0, n):",
            font_size=16
        )

        solEq4 = MathTex(
            r"I(\alpha, 0, n) = \int_{1}^{\infty} \frac{x^{\alpha}(1 - x)}{1 - x^{n+1}} \, \mathrm{d}x",
            font_size=16
        )

        # Cambio de variable
        texto5 = MathTex(
            r"\text{Haciendo el cambio de variable } x = t^{-1/(n+1)}:",
            font_size=16
        )

        solEq5 = MathTex(
            r"x = t^{-1/(n+1)}, \quad \mathrm{d}x = -\frac{1}{n+1}t^{-(n+2)/(n+1)} \, \mathrm{d}t",
            font_size=16
        )

        # Integral después del cambio de variable
        texto6 = MathTex(
            r"\text{Simplificando la expresión:}",
            font_size=16
        )

        solEq6 = MathTex(
            r"I(\alpha, 0, n) = \frac{1}{n+1}\int_{0}^{1} \frac{t^{-(\alpha+1)/(n+1)}(1 - t^{-1/(n+1)})}{t-1} \, \mathrm{d}t",
            font_size=16
        )

        # Reorganización del denominador
        solEq7 = MathTex(
            r"I(\alpha, 0, n) = -\frac{1}{n+1} \int_{0}^{1} \frac{t^{-(\alpha+1)/(n+1)} - t^{-(\alpha+2)/(n+1)}}{1-t} \, \mathrm{d}t",
            font_size=16
        )

        # Propiedad de la función Digamma
        texto7 = MathTex(
            r"\text{Aplicando la propiedad de la función Digamma:}",
            font_size=16
        )

        solEq8 = MathTex(
            r"\int_{0}^{1} \frac{t^{p-1} - t^{q-1}}{1 - t} \, \mathrm{d}t = \psi(q) - \psi(p), \quad \Re(p), \Re(q) > 0",
            font_size=16
        )

        # Solución para b=0
        texto8 = MathTex(
            r"\text{Solución para } b=0:",
            font_size=16
        )

        solEq9 = MathTex(
            r"I(\alpha, 0, n) = \frac{1}{n+1} \left[ \psi\left(1-\frac{\alpha+1}{n+1}\right) - \psi\left(1-\frac{\alpha+2}{n+1}\right) \right]",
            font_size=16
        )

        # Diferenciación bajo el signo integral
        texto9 = MathTex(
            r"\text{Diferenciando bajo el signo integral:}",
            font_size=16
        )

        solEq16 = MathTex(
            r"I(\alpha, b, n) = \frac{\partial^b}{\partial \alpha^b} I(\alpha, 0, n)",
            font_size=16
        )

        # Derivada de la función Digamma
        texto16 = MathTex(
            r"\text{Derivada de la función Digamma:}",
            font_size=16
        )

        solEq11 = MathTex(
            r"\frac{\mathrm{d}^b}{\mathrm{d} \alpha^b} \psi(f) = \psi^{(b)}(f) \cdot \left( \frac{\mathrm{d}f}{\mathrm{d}\alpha} \right)^b",
            font_size=16
        )

        # Solución general final
        texto11 = MathTex(
            r"\text{Solución general final:}",
            font_size=16
        )

        solEq12 = MathTex(
            r"I(\alpha, b, n) = \frac{(-1)^b}{(n+1)^{b+1}} \left[ \psi^{(b)}\left(1-\frac{\alpha+1}{n+1}\right) - \psi^{(b)}\left(1-\frac{\alpha+2}{n+1}\right) \right]",
            font_size=16
        )

        # Agrupar las ecuaciones en una lista para manejarlas
        equations = [
            texto1, solEq1, texto2, solEq2, texto3, solEq3, texto4, solEq4,
            texto5, solEq5, texto6, solEq6, solEq7, texto7, solEq8, texto8, 
            solEq9, texto9, solEq16, texto16, solEq11, texto11, solEq12
        ]

        # Ajustar espaciado y mostrar las ecuaciones una por una 
        self.play(FadeIn(texto1, shift=UP*4))
        self.wait(0.5)

        self.play(Write(solEq1))
        self.wait(1)
        self.play(solEq1.animate.shift(UP * 1.5))
        self.wait(0.5)

        # Posiciona solEq2 donde estaba solEq1 inicialmente y luego hazla aparecer
        solEq2.move_to(solEq1.get_center() - UP * 1.5)  # Ajusta la posición
        self.play(FadeIn(solEq2))
        self.wait(1)
