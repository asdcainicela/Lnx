from manim import *
from LnxScene import * 


class MathProblems(Scene):
    def construct(self): 
         
        
        # Basic Level
        basic_title = Tex(r"\textbf{Nivel Básico}", font_size=30)
        self.play(Write(basic_title))
        self.wait(0.5)
        
        prob1 = MathTex(
            r"\int_0^1 \ln^2(1+x^2) \, dx",
            font_size=25
        )
        
        prob2 = MathTex(
            r"\int_0^{\pi} \frac{\sin x}{\sqrt{\sin x} + 1} \, dx",
            font_size=25
        )
        
        # Intermediate Level
        intermediate_title = Tex(r"\textbf{Nivel Intermedio}", font_size=30)
        
        prob3 = MathTex(
            r"A(x) = \begin{pmatrix} x^{x^{x^{x^x}}} & \sin^5(x-1) \\ (x-1)^5 & x^{x^{x^x}} \end{pmatrix}",
            font_size=25
        )
        
        prob4 = MathTex(
            r"\lim_{x \to 1} \frac{(a_n(x) - d_n(x))b_n(x)}{c_n^2(x)}",
            font_size=25
        )
        
        prob5 = MathTex(
            r"\int_0^\infty \frac{\cos x}{\cosh^{2n+1} x} \, dx \quad (n \in \mathbb{N}_0)",
            font_size=25
        )
        
        # Advanced Level
        advanced_title = Tex(r"\textbf{Nivel Avanzado}", font_size=30)
        
        prob6 = MathTex(
            r"A = \begin{pmatrix} a & b \\ b & a \end{pmatrix}, \quad \int_0^\infty \frac{\cos(Ax) + x \sin(Ax)}{x^2 + 1} \, dx",
            font_size=25
        )
        
        prob7 = MathTex(
            r"\int_{-1}^1 \frac{\ln^2(1+x^2)}{\sqrt{1-x^2}} \, dx",
            font_size=25
        )
        
        prob8 = MathTex(
            r"\int_0^1 \text{Li}_{5}{(x)}   \text{Li}_{6}{(x)}  \, dx",
            font_size=25
        )
        
        polylog_def = MathTex(
            r"\text{Donde }  \text{Li}_{n}{(x)}  = \sum_{k=1}^\infty \frac{x^k}{k^n} \text{ para } |x| \leq 1",
            font_size=25
        )
        
        # Expert Level
        expert_title = Tex(r"\textbf{Nivel Experto}", font_size=30)
        
        prob9 = MathTex(
            r"\lim_{n \to \infty} \left[ n^2 \ln \left( \lim_{t \to 0^+} \left( \int_0^1 \frac{dx}{\sqrt[n]{x^n + t^n}} + \ln t \right) \right) \right]",
            font_size=25
        )
        
        prob10 = MathTex(
            r"\lim_{x \to \infty} \left[ \frac{1}{x} \left( \frac{\zeta\left(1 + \frac{1}{x}\right)}{x} \right)^{\frac{x}{\gamma}}"
            r"\left( \frac{(2x)!}{x!} \right)^{\frac{1}{x}} - 4 \right] x",
            font_size=25
        )

        
        prob10_explanation = MathTex(
            r"\text{Donde } \zeta(s) \text{ es la función zeta de Riemann}",
            r"\gamma \text{ es la constante de Euler-Mascheroni}",
            font_size=20
        )
        
        # Add animations here
        self.play(Write(prob1))
        self.wait(2)
        self.play(ReplacementTransform(prob1, prob2))
        self.wait(2)
        # Continue with other problems...