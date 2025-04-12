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
            'width': 4.2,
            'height': 2.5,
            'image_path': None,
            'image_scale': 1/4,
            'image_buff': 0.5,
            'box_display_time': 3.0,
            'box_fill_color': "#1f1f1f",
            'box_stroke_color': GOLD,
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
            self.scene.wait(0.1)
        
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
            Create(self.box, run_time=0.5),
            UpdateFromFunc(self.tracer, lambda m: m.move_to(self.box.get_end())),
            run_time=0.5
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
        self.scene.add(self.box)
    
    def off(self):
        if not self.box:
            raise ValueError("Debes activar primero con on()")
        
        self.scene.play(
            FadeOut(self.box),
            FadeOut(self.fill),
            FadeOut(self.imagen),
            run_time=0.8
        )

def logo_handler(scene, existing_logo=None, image_path=None, corner=DR, 
                animation_style="elastic", initial_scale=0.4, target_scale=0.4*0.4, 
                buff=0.25, fade_in=True):
    """
    Función universal para manejo de logos:
    
    1. Si existe existing_logo: Lo mueve a la esquina
    2. Si no existe: Carga image_path y lo anima desde el centro
    
    Parámetros:
    - existing_logo: Objeto de imagen existente (opcional)
    - image_path: Ruta si no hay logo existente (requerido si existing_logo es None)
    - corner: DR (default), DL, UR, UL
    - animation_style: "smooth", "elastic", "rush"
    - initial_scale: Escala inicial (solo para nuevo logo)
    - target_scale: Escala al finalizar animación
    - buff: Espacio desde la esquina
    - fade_in: Animación de entrada para nuevo logo
    """
    
    # Validación básica
    if existing_logo is None and image_path is None:
        raise ValueError("Debe proveer existing_logo o image_path")

    # Configuración de animación
    anim_config = {
        "smooth": {"rate_func": smooth, "run_time": 1.5},
        "elastic": {"rate_func": rate_functions.ease_out_elastic, "run_time": 2.0},
        "rush": {"rate_func": rate_functions.rush_into, "run_time": 0.8},
        "fast": {"rate_func": rate_functions.ease_out_elastic, "run_time": 0.2},
    }
    
    # Caso 1: Logo existente
    if existing_logo is not None:
        logo = existing_logo
        scene.play(
            logo.animate.to_corner(corner, buff=buff).scale(target_scale),
            **anim_config[animation_style]
        )
    
    # Caso 2: Nuevo logo
    else:
        logo = ImageMobject(image_path).scale(initial_scale).move_to(ORIGIN)
        
        if fade_in:
            scene.play(FadeIn(logo, shift=UP*0.3), run_time=0.1)
        
        scene.play(
            logo.animate.to_corner(corner, buff=buff).scale(target_scale),
            **anim_config[animation_style]
        )
    
    return logo

## finalizar el logo aquí va
def animate_End(scene, svg_path="logo.svg", scale_factor=0.4, colors=[YELLOW, ORANGE]):
    """
    Función que anima un logo SVG en una escena de Manim.
    
    Args:
        scene (Scene): Instancia de la escena Manim donde se añadirá la animación.
        svg_path (str): Ruta del archivo SVG. Por defecto: "logo.svg".
        scale_factor (float): Escala del logo. Por defecto: 0.5.
        colors (list): Lista de colores para el gradiente del contorno. Por defecto: [YELLOW, ORANGE].
    """
    logo = SVGMobject(svg_path).scale(scale_factor)

    scene.clear()
    # Animación del contorno
    outline_path = VMobject()
    for submobject in logo:
        outline_path.append_points(submobject.get_points())
    outline_path.set_stroke(color=colors, width=2)
    
    scene.play(Create(outline_path), run_time=0.5) 
    scene.play(
        FadeOut(outline_path,run_time=0.5),
        FadeIn(logo, run_time=0.5),
        lag_ratio=0
        )
    scene.wait(0.5)





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

def grillado(scene):
    # Crear la grilla
    grid = NumberPlane(
        x_range=[-4, 4, 0.3],  # Rango del eje X
        y_range=[-6, 6, 0.3],    # Rango del eje Y
        background_line_style={
            "stroke_color": RED,  # Color de las líneas
            "stroke_width": 0.5,     # Grosor de las líneas
            "stroke_opacity": 0.1, # Opacidad de las líneas
        },
        axis_config={"stroke_opacity": 0},  # Ocultar los ejes
    )
    scene.add(grid)  # Agregar la grilla a la escena