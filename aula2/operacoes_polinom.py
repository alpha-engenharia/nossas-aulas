from numpy import polyadd, polysub, polymul, polydiv

p1 = [4, 6, 3, 2]   # coeficientes de 4x³ + 6x + 3x + 2 
p2 = [2, 1, 2]      # coeficientes de 2x² + x + 2

soma = polyadd(p1, p2)
subtracao = polysub(p1, p2)
multiplicacao = polymul(p1, p2)
divisao = polydiv(p1, p2)

print("Quociente =", divisao[0], "resto =", divisao[1])