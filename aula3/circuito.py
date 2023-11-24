from numpy import matrix

A = matrix([
    [10 - 5j, 5j],
    [5j, 3 - 1j]
])

B = matrix([
    [50],
    [0]
])

X = A**-1 * B

print(X)