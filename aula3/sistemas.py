from numpy import matrix

A = matrix([
    [3, -1, 1],
    [-2, 3, -3],
    [-1, -3, -4]
])

B = matrix([
    [11],
    [-19],
    [-15]
])

X = A**-1 * B

print(X)