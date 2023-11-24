from numpy import matrix, transpose, linalg

C = matrix([[7, 2, 4],
            [3, 5, 9],
            [1, 6, 8]])

C_t = transpose(C)
det_C = linalg.det(C)
C_inv = C ** -1

print(C_inv)