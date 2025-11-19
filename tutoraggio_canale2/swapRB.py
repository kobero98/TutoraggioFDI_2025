def swapRB(pict):
    # @param pict: immagine da processare
    # 1) Prendo la sequenza di pixel
    pixels = getPixels(pict)
    # 2) Scorro tutti i pixel
    for i in range(0, len(pixels)):
        px = pixels[i]
        # 3) Leggo i canali
        r = getRed(px)
        b = getBlue(px)
        # 4) Controllo la condizione
        if r < b:
            # 5) Assegno a Red il valore di Blue
            setRed(px, b)
            # 6) Assegno a Blue il valore Red
            setBlue(px, r)

pict = makePicture(pickAFile())
swapRB(pict)
repaint(pict)