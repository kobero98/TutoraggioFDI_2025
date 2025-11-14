def esercizio1_gestioneImmagine(pict):
    #@Param pict:Picture
    vPixels = getPixels(pict)
    #primo pixel
    fPixel = vPixels[0]
    fColor = getColor(fPixels)
    print "il colore del primo pixel e'",fColor

    #ultimo pixel
    lPixel = vPixels[len(vPixels)-1]
    lColor = getColor(lPixels)
    print "il colore dell'ultimo pixel e'",lColor


