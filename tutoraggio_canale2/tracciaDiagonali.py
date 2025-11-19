def tracciaDiagonali(pict, col):
    # @param pict: Picture
    # @param col: Color
    # Disegna le due diagonali in cicli distinti
    w = getWidth(pict)
    h = getHeight(pict)
    
    n = min(w, h)
    
    # 1) Diagonale principale
    for i in range(0, n):
        x = i
        y = i
        setColor(getPixel(pict, x, y), col)
        
    # 2) Antidiagonale
    for j in range(0, n):
        x = n - 1 - j
        y = j
        setColor(getPixel(pict, x, y), col)

pict = makePicture(pickAFile())
tracciaDiagonali(pict, green)
repaint(pict)