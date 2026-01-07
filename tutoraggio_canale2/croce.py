def croce(A, i, j):
    # controlli indici
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return False
    return riga(A, i, j) and colonna(A, i, j)

def riga(A, i, j):
    aij = A[i][j]
    # vicino sinistro (se esiste)
    if j - 1 >= 0 and aij <= A[i][j-1]:
        return False
    # vicino destro (se esiste)
    if j + 1 < len(A[0]) and aij <= A[i][j+1]:
        return False
    return True

def colonna(A, i, j):
    aij = A[i][j]
    # vicino sopra (se esiste)
    if i - 1 >= 0 and aij <= A[i-1][j]:
        return False
    # vicino sotto (se esiste)
    if i + 1 < len(A) and aij <= A[i+1][j]:
        return False
    return True

A = [[1, 2, 3, 10],[3, 5, 7, 2],[8, 1, 4, 6],[4, 9, 2, 5]]
print(A)
print(croce(A, 0, 0))
print(croce(A, 0, 3))