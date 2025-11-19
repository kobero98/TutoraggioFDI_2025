def privacy2_safe(pict, xmin, xmax, ymin, ymax):
    # @param pict: Picture
    # @param xmin, xmax, ymin, ymax: int
    # Effetto: oscura il rettangolo compreso tra (xmin, ymin) e (xmax, ymax)
    w = getWidth(pict)
    h = getHeight(pict)
    
    # 1) Ordino le coppie
    left0 = min(xmin, xmax)
    right0 = max(xmin, xmax)
    top0 = min(ymin, ymax)
    bot0 = max(ymin, ymax)
    
    # 2) Fisso i bordi evitando valori negativi o fuori dall'immagine
    left = min(max(0, left0), w - 1)
    right = min(max(0, right0), w - 1)
    top = min(max(0, top0), h - 1)
    bottom = min(max(0, bot0), h - 1)
    
    # 3) Disegno sul rettangolo
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            p = getPixel(pict, x, y)
            setColor(p, black)

pict = makePicture(pickAFile())
privacy2_safe(pict, 200, 500, 300, 600)
repaint(pict)