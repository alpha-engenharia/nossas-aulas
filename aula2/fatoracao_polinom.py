from sympy.abc import x
from sympy import factor

pol = x**3 - 3*x**2 - 10*x + 24

fator = factor(pol)

print(f"A fatoração de {pol} é {fator}")