def enigma2(pict, col, k):
    # @param pict: picture
    # @param col: color
    # @param k: int
    for x in range(0, min(getWidth(pict), getHeight(pict))):
        px = getPixel(pict, x, x+k)
        setColor(px, col)

pict = makePicture(pickAFile())
enigma2(pict, pink, 100)
repaint(pict)