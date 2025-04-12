from manim import *

def grillado(scene):
    # Crear la grilla
    grid = NumberPlane(
        x_range=[-10, 10, 1],  # Rango del eje X
        y_range=[-6, 6, 1],    # Rango del eje Y
        background_line_style={
            "stroke_color": BLUE,  # Color de las líneas
            "stroke_width": 1,     # Grosor de las líneas
            "stroke_opacity": 0.5, # Opacidad de las líneas
        }
    )
    scene.add(grid)  # Agregar la grilla a la escena



class LinearEquation(Scene):
    def construct(self):
        self.camera.background_color = "#111317" 
        expr = MathTex(r" \frac{2x+5}{3} = 7 ", font_size=55).shift(UP * 1)

        question = MathTex(r"x=?", font_size=50).next_to(expr, DOWN, buff=1.3)  

        rect = SurroundingRectangle(
            question,
            buff=0.25,
            corner_radius=0.1,
            color=[YELLOW]
            )
        
        grillado(self)

        self.play(Write(expr))
        self.wait(1) 
        self.play(
            Succession(
                Wait(1.0), 
                Write(question), 
            ),
            Create(rect, run_time=1.0),
        ) 
        self.wait(2)  





 