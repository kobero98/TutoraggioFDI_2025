def getMinLum(pict):
    pixs = getPixels(pict)
    # 1) Inizializzo a 765 (massimo possibile di r+g+b)
    minLum = 255 + 255 + 255
    
    # 2) Scorro tutti i pixel
    for i in range(0, len(pixs)):
        px = pixs[i]
        # 2.1) Componenti
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        # 2.2) Somme a step
        lum = r + g + b
        
        # 2.3) Aggiornamento del minimo
        if lum < minLum:
            minLum = lum
            
    # 3) Ritorno il minimo
    return minLum

pict = makePicture(pickAFile())
lum = getMinLum(pict)
print(lum)