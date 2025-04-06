# Archivo LnxScene.py
from manim import *
from PIL import Image

class MathPazoKpTemplate(TexTemplate):
    def __init__(self):
        super().__init__()
        self.preamble = r"""
        \usepackage{mathpazo}
        \usepackage[nomath]{kpfonts}
        \usepackage[T1]{fontenc}
        \usepackage[spanish]{babel}
        \usepackage{amsmath} 
        """

def backgroundLnx(scene, fondo="#111111"):
    scene.camera.background_color = fondo

class BoxAnimation:
    def __init__(self, scene, **kwargs):
        self.scene = scene
        self.box = None
        self.fill = None
        self.imagen = None
        self.tracer = None
        self.params = {
            'width': 4.0,
            'height': 2.5,
            'image_path': None,
            'image_scale': 1/4,
            'image_buff': 0.5,
            'box_display_time': 3.0,
            'box_fill_color': "#1f1f1f",
            'box_stroke_color': "#ffff00",
            'corner_radius': 0.15,
            'stroke_width': 2
        }
        self.params.update(kwargs)
    
    def on(self):
        # Paso 1: Imagen
        if self.params['image_path']:
            self.imagen = ImageMobject(self.params['image_path'])
            self.imagen.scale(self.params['image_scale']).move_to(ORIGIN)
            self.scene.add(self.imagen)
            self.scene.wait(0.5)
        
        # Paso 2-3: Creación del rectángulo y posición de imagen
        self.box = RoundedRectangle(
            width=self.params['width'],
            height=self.params['height'],
            corner_radius=self.params['corner_radius'],
            stroke_width=self.params['stroke_width'],
            fill_opacity=0,
            stroke_color=[YELLOW, ORANGE, "#FF8C00"]
        )
        
        if self.imagen:
            self.imagen.next_to(self.box, DOWN, buff=self.params['image_buff'])
        
        # Paso 4: Animación de creación con tracer
        self.tracer = Dot(color=RED, radius=0.08)
        self.scene.add(self.tracer)
        self.tracer.move_to(self.box.get_bottom())
        
        self.scene.play(
            Create(self.box, run_time=0.8),
            UpdateFromFunc(self.tracer, lambda m: m.move_to(self.box.get_end())),
            run_time=0.8
        )
        self.scene.play(FadeOut(self.tracer))
        
        # Paso 5-6 modificados: Fondo y borde instantáneo
        self.fill = self.box.copy().set_style(
            fill_color=self.params['box_fill_color'],  
            fill_opacity=1,
            stroke_width=0
        )
        self.scene.add(self.fill)
        self.fill.z_index = -1
        
        # Cambio de color de borde inmediato
        self.box.set_stroke(color=self.params['box_stroke_color'])
        self.scene.add(self.box)  # Refrescar render
    
    def off(self):
        if not self.box:
            raise ValueError("Debes activar primero con on()")
        
        self.scene.play(
            FadeOut(self.box),
            FadeOut(self.fill),
            run_time=1.0
        )
        
        if self.imagen:
            self.scene.play(
                self.imagen.animate.scale(0.4).to_corner(DL),
                run_time=1
            )
        
        self.scene.wait(1)

class SmartMathTex(MathTex):
    def __init__(self, tex, target_width, target_height, **kwargs):
        super().__init__(tex, **kwargs)
        self.initial_font_size = self.font_size
        self.target_width = target_width
        self.target_height = target_height
        self.auto_scale()

    def auto_scale(self):
        width_ratio = self.target_width / self.width
        height_ratio = self.target_height / self.height
        scale_factor = min(width_ratio, height_ratio, 1.0)
        self.scale(scale_factor * 0.95)
        self.font_size = self.initial_font_size * scale_factor