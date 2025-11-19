def draw_rect(pict, x0, y0, width, height, color):
    # @param pict: Picture
    # @param x0: int (coordinata iniziale orizzontale)
    # @param y0: int (coordinata iniziale verticale)
    # @param width: int (larghezza del rettangolo)
    # @param height: int (altezza del rettangolo)
    # @param color: Color
    W = getWidth(pict)
    H = getHeight(pict)
    xEnd = min(x0 + width, W)
    yEnd = min(y0 + height, H)
    
    for y in range(y0, yEnd):
        for x in range(x0, xEnd):
            if (0 <= x < W) and (0 <= y < H):
                setColor(getPixel(pict, x, y), color)

pict = makePicture(pickAFile())
draw_rect(pict, 200, 300, 400, 500, pink)
repaint(pict)