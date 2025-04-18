from manim import *

 

class Intro(ThreeDScene):
	def construct(self):
		 
					
		title = Title("Volúmen en 3D", font_size=30).shift(DOWN*0.5)
		title.set_color_by_gradient(ORANGE, YELLOW)

		#text1 = Text("Today we will see the ", font_size=50)
		#text2 = Text("volume of different 3d shapes", font_size=50).next_to(text1, DOWN)

		self.play(Write(title))
		self.wait(1)
		#self.play(AddTextLetterByLetter(text1, run_time=0.5))
		#self.play(AddTextLetterByLetter(text2, run_time=0.5))
		#self.wait(2)
		#self.play(FadeOut(VGroup(title, text1, text2)))
		self.play(FadeOut( title ))
		#self.wait(2)

		CuboidVolume.construct(self)


class CuboidVolume(ThreeDScene):
	def construct(self):
		title = MathTex(r"\text{Paralelepipedo}", font_size=35).shift(UP*2.7).set_color_by_gradient(BLUE_A,   BLUE)

		scaleValue= 0.1
		sizeCubo = 2
		

		length = MathTex("l", font_size=25, color=YELLOW).next_to(title, DOWN, buff=1)
		area = MathTex("l", r"\cdot", "b", font_size=25, color=GOLD).next_to(title, DOWN, buff=1)
		volume = MathTex("l", r"\cdot", "b", r"\cdot", "h", font_size=25, color=ORANGE).next_to(title, DOWN, buff=1) 
		label = [
			MathTex(r"\text{longitud}", font_size=25, color=YELLOW_D).next_to(length, UP, buff=0.3),
			MathTex(r"\text{área}", font_size=25, color=GOLD_B).next_to(area, UP, buff=0.3),
			MathTex(r"\text{volumen}", font_size=25, color=GOLD_D).next_to(volume, UP, buff=0.3),
        ]
		
		dot = Dot()
		line = Rectangle(width=sizeCubo, height=0.0000001, color=BLUE_A)
		rect = Rectangle(width=sizeCubo, height=sizeCubo/2 , color=BLUE_D)
		cuboid = Prism(
            dimensions=[sizeCubo, sizeCubo/2, sizeCubo/2],  # Ancho, profundidad, altura
            fill_opacity=0.3,      # Opacidad del relleno (0 para solo borde)
            #fill_color=RED,       # Color del relleno
            stroke_color=WHITE,   # Color del borde
            stroke_width=2,      # Grosor del borde
        )
		#cuboid.rotate(-10 * DEGREES, Y_AXIS).rotate(-90 * DEGREES, X_AXIS).rotate(45 * DEGREES, Y_AXIS).shift([0, 0, 0])
		cuboid.rotate(45*DEGREES, Y_AXIS)      # Primera rotación horizontal
		cuboid.rotate(35.264*DEGREES, X_AXIS)  # Ángulo mágico isométrico
	
		self.play(Create(title))
		self.play(Create(dot))
		self.wait(0.2)
		self.play(ReplacementTransform(dot, line), Write(length), Write(label[0]))
		self.wait(1)
		self.play(ReplacementTransform(line, rect), TransformMatchingTex(length, area),
		          TransformMatchingShapes(label[0], label[1]))
		self.wait(1)
		self.play(rect.animate.shift([0, -1, 0]))
		self.play(Rotate(rect, -90 * DEGREES, X_AXIS))
		self.wait(0.000000001)
		self.play(Rotate(rect, 45 * DEGREES, Y_AXIS))
		self.play(Transform(rect, cuboid), TransformMatchingTex(area, volume),
		          TransformMatchingShapes(label[1], label[2]))
		self.wait(1.5)
		self.play(FadeOut(title, volume, label[2]))
		self.remove(cuboid, rect)
		self.wait(2)
		#SphereVolume.construct(self)

class CylinderVolume(ThreeDScene):
	def construct(self):
		rect_style = {
							"stroke_width": 4,
							"fill_opacity": 0
					}
   
      # Crear rectángulos con parámetros específicos
		rectangles = VGroup(
            Rectangle(width=4, height=7.6, color=YELLOW, **rect_style),
            Rectangle(width=3.5, height=6, color=GREEN, **rect_style)
        )
		self.add(rectangles)
  
		title = MathTex(r"\text{Cilindro}", font_size=35).shift(UP*2.7).set_color_by_gradient(BLUE_A,   BLUE)


		radius = MathTex("r", font_size=25, color=BLUE_B).next_to(title, DOWN, buff=1)
		area = MathTex(r"\pi", r"\cdot", "r^{2}", font_size=25, color=LIGHT_GRAY).next_to(title, DOWN, buff=1)
		volume = MathTex(r"\pi", r"\cdot", "r^{2}", "\cdot", "h", font_size=25, color=BLUE_C).next_to(title, DOWN, buff=1)

		label = [
				Text("radius", font_size=25, color=BLUE_E).next_to(radius, UP, buff=0.3),
				Text("area", font_size=25, color=LIGHT_GRAY).next_to(area, UP, buff=0.3),
				Text("volume", font_size=25, color=BLUE_D).next_to(volume, UP, buff=0.3),
		]

		dot = Dot().shift([0, -1/2, 0])
		line = Line([0, -1/2, 0], [1.3/2, -1/2, 0], color= DARK_BLUE)
		circle = Circle(radius=1.3/2, color=BLUE_B).shift([0, -1/2, 0])
  
  

		cylinder = Cylinder(1.3/2, 4/2, Y_AXIS).shift([0, -1/2, 0])
		 

		self.play(Create(title))
		self.wait(0.5)
		self.play(Create(dot))
		self.play(Create(line), Write(radius), Write(label[0]))
		self.wait(1)
		self.play(Create(circle, run_time=1),
		          Rotate(line, 360 * DEGREES, run_time=1, about_point=[0, -1/2, 0]),
		          TransformMatchingTex(radius, area),
		          TransformMatchingShapes(label[0], label[1]))
		self.wait(1)
		self.play(FadeOut(line, dot))
		self.wait(1)
		self.play(circle.animate.shift([0, -2/2, 0]))
		self.play(Rotate(circle, -90 * DEGREES, X_AXIS))
		self.wait(0.000000001)
		self.play(Rotate(circle, 45 * DEGREES, Y_AXIS))
		self.wait(1)
		self.play(Transform(circle, cylinder),
		          TransformMatchingTex(area, volume),
		          TransformMatchingShapes(label[1], label[2]))
		self.wait(2)
		self.play(FadeOut(VGroup(title, volume, label[2], cylinder, circle)))
		self.wait(2)
		