def changeCRowColumn(pict, n):
    # @param pict: Picture
    # @param n: integer
    # @return Picture
    if not getWidth(pict)==getHeight(pict):
        return pict
    if not 0<=n<=getWidth(pict):
        return pict
    for i in range(0, getWidth(pict)):
        px1 = getPixel(pict, i, n)
        px2 = getPixel(pict, n, i)
        col1 = getColor(px1)
        col2 = getColor(px2)
        setColor(px1, col2)
        setColor(px2, col1)
    return pict

pict = makePicture(pickAFile())
show(pict)
pict2 = changeCRowColumn(pict, 100)

def changeNRowColumn(matrix, n):
    # @param matrix: List of List of Integer
    # @param n: integer
    # @return List of List of Integer
    if not len(matrix)==len(matrix[0]):
        return matrix
    if not 0<=n<=len(matrix):
        return matrix
    for i in range(0, len(matrix)):
        x1 = matrix[i][n]
        x2 = matrix[n][i]
        matrix[i][n] = x2
        matrix[n][i] = x1
    return matrix

matrix = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(matrix)
print()
print(changeNRowColumn(matrix, 2))