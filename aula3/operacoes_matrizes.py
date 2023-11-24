from numpy import matrix

A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

B = matrix([
    [3, 6, 9],
    [1, 8, 2],
    [1, 2, 3]
])

#soma = A + B
#subtracao = A - B
multiplicacao = A * B
escalar = 2 * A
#expressao = 2 * A + 5 * B
quadrado = B ** 2

print(quadrado)