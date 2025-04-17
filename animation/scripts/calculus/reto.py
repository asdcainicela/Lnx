from manim import *
from LnxScene import *


class MathProblems(Scene):
    def construct(self):
        backgroundLnx(self) 
        self.camera.tex_template = MathPazoKpTemplate()
         
        title=  Tex(r"\textbf{Desafío a la Comunidad}", font_size=25).shift(UP * 2.3)
        title.set_color_by_gradient(ORANGE, RED) 
        self.play(Write(title))

        # Basic Level
        basic_title = Tex(r"\textbf{Nivel Básico}", font_size=30).next_to(title, DOWN, buff=0.5)  
        basic_title.set_color(YELLOW) # Aplicar gradiente de colores
        self.play(Write(basic_title))
        self.wait(0.5)
        
        prob1 = MathTex(
            r"\int_0^{\pi} \frac{\sin x}{\sqrt{\sin x} + 1} \, dx",
            font_size=20
        ).next_to(basic_title, DOWN, buff=0.5) 
        
        prob2 = MathTex(
            r"\int_0^1 \ln^2(1+x^2) \, dx",
            font_size=20
        ).next_to(prob1, DOWN, buff=0.5) 

        # Add animations here
        self.play(Write(prob1))
        self.wait(1)
        self.play(Write(prob2))
        self.wait(1)
        
        # Intermediate Level
        intermediate_title = Tex(r"\textbf{Nivel Intermedio}", font_size=30).next_to(title, DOWN, buff=0.5)  
        intermediate_title.set_color(YELLOW)
        #-----------------
        

        prob3 = MathTex(
            r"A(x) = \begin{pmatrix} x^{x^{x^{x^x}}} & \sin^5(x-1) \\ (x-1)^5 & x^{x^{x^x}} \end{pmatrix} \\[10pt]",  # 10pt de espacio extra
            r"\lim_{x \to 1} \frac{(a_n(x) - d_n(x))b_n(x)}{c_n^2(x)}",
            #tex_environment="align*",  # Entorno alineado (opcional)
            font_size=18
        ).next_to(intermediate_title, DOWN, buff=0.5)
        
        
        prob4 = MathTex(
            r"\int_{0}^{\infty} \frac{\ln^2(x)}{\cosh(x)  } dx", 
            font_size=20
        ).next_to(prob3, DOWN, buff=0.4) 
        
        prob5 = MathTex(
            r"	\int_0^{\infty} \frac{\ln(1+x^2)}{(1+x^3)^3} dx",
            font_size=20
        ).next_to(prob4, DOWN, buff=0.4) 

        self.play(Transform(basic_title, intermediate_title),
                  FadeOut(prob1),
                  FadeOut(prob2)
                  )
        self.play(Write(prob3))
        self.wait(1)
        self.play(Write(prob4))
        self.wait(1)
        self.play(Write(prob5))
        self.wait(1)
 #------------------------------       
        # Advanced Level
        advanced_title = Tex(r"\textbf{Nivel Avanzado}", font_size=30).next_to(title, DOWN, buff=0.4)  
        
       

        prob6 = MathTex(
            r" A = \begin{pmatrix} a & b \\ b & a \end{pmatrix}, \\[10pt]",  # 10pt de espacio extra
            r"\int_0^\infty \frac{\cos(Ax) + x \sin(Ax)}{x^2 + 1} \, dx",
            #tex_environment="align*",  # Entorno alineado (opcional)
            font_size=18
        ).next_to(advanced_title, DOWN, buff=0.5)
        
        prob7 = MathTex(
            r"\int_{-1}^1 \frac{\ln^2(1+x^2)}{\sqrt{1-x^2}} \, dx",
            font_size=20
        ).next_to(prob6, DOWN, buff=0.4) 
        
        prob8 = MathTex(
            r"\int_0^1 \text{Li}_{5}{(x)}   \text{Li}_{6}{(x)}  \, dx",
            font_size=20
        ).next_to(prob7, DOWN, buff=0.4) 
        
        polylog_def = MathTex(
            r"\text{Donde }  \text{Li}_{n}{(x)}  = \sum_{k=1}^\infty \frac{x^k}{k^n} \text{ para } |x| \leq 1",
            font_size=25
        )
        
        self.play(Transform( intermediate_title, advanced_title ),
                        FadeOut(prob3),
                        FadeOut(prob4),
                        FadeOut(prob5),
                        FadeOut(basic_title)
                        )
        self.play(Write(prob6))
        self.wait(1)
        self.play(Write(prob7))
        self.wait(1)
        self.play(Write(prob8))
        self.wait(1)

        # Expert Level
        expert_title = Tex(r"\textbf{Nivel Experto}", font_size=30).next_to(title, DOWN, buff=0.4)  
        
        prob9 = MathTex(
            r"\lim_{n \to \infty} \left[ n^2 \ln \left( \lim_{t \to 0^+} \left( \int_0^1 \frac{dx}{\sqrt[n]{x^n + t^n}} + \ln t \right) \right) \right]",
            font_size=18
        ).next_to(advanced_title, DOWN, buff=0.4) 
        
        prob10 = MathTex(
            r"\lim_{x \to \infty} \left[ \frac{1}{x} \left( \frac{\zeta\left(1 + \frac{1}{x}\right)}{x} \right)^{\frac{x}{\gamma}}"
            r"\left( \frac{(2x)!}{x!} \right)^{\frac{1}{x}} - 4 \right] x",
            font_size=18
        ).next_to(prob9, DOWN, buff=0.4) 

        
        prob10_explanation = MathTex(
            r"\text{Donde } \zeta(s) \text{ es la función zeta de Riemann}",
            r"\gamma \text{ es la constante de Euler-Mascheroni}",
            font_size=20
        ).next_to(advanced_title, DOWN, buff=0.4) 
        
        self.play(Transform( advanced_title, expert_title  ),
                        FadeOut(prob6),
                        FadeOut(prob7),
                        FadeOut(prob8),
                        FadeOut(intermediate_title)
                        )
        self.play(Write(prob9))
        self.wait(1)
        self.play(Write(prob10))
        
        self.wait(5)