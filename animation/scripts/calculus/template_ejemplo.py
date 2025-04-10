from manim import *
from LnxScene import *

# Clase principal de animación
class CompleteAnimation(Scene):
    def construct(self):
        # Fondo personalizado (probablemente con color o imagen)
        backgroundLnx(self)

        # Establecer el template LaTeX con fuentes elegantes (mathpazo + kpfonts)
        self.camera.tex_template = MathPazoKpTemplate()

        box_anim = BoxAnimation( self, image_path="logo.png",  )
        box_anim.on()
        
        # 2. Mover logo con ajustes
        #logo_handler(  scene=self, image_path="logo.png" )
        
        # 4. El resto de tu lógica original
        self.wait(2)
        box_anim.off()
        
        #------------------------------------------
 
        # TEXTO: Enunciado del problema
        texto1 = MathTex( 
            r"\text{Ejemplo de plantilla de Lnx} ",
            font_size=22
        )
 
        # ANIMACIONES de entrada: Escritura tipo "dibujado"
        self.play(Write(texto1),run_time=0.5)  # Escribir el enunciado
        self.wait(0.5)  
        #self.wait(1) 
        animate_End( scene=self, svg_path="logo.svg" ) # finalizar con logo
 



 