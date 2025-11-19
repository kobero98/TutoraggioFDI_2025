def mediaRed(pict, K):
    # @param pict: Picture - immagine d'ingresso
    # @param K: int - soglia per la coordinata x (larghezza)  
    # Effetto: stampa la media aritmetica di Red per tutti i pixel con x <= K.
    w = getWidth(pict)
    h = getHeight(pict)
    
    # 1) Fisso K tra [0, w-1]
    k1 = min(K, w - 1)
    kOK = max(0, k1)
    
    somma = 0
    conteggio = 0
    
    # 2) Visitiamo le colonne
    for y in range(0, h):
        for x in range(0, kOK + 1):
            px = getPixel(pict, x, y)
            r = getRed(px)
            somma = somma + r
            conteggio = conteggio + 1
    
    # 3) Media
    media = somma / conteggio
    print(media)

mediaRed(makePicture(pickAFile()), 100)