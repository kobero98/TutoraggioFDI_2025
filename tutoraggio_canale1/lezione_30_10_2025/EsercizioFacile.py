def esercizioFacileA(pict):
    # @Param pict:Picture
    listPixels = getPixels(pict)
    for index in range(0,len(listPixels)):
        p = listPixels[index]
        cRed = getRed(p)
        cGreen = getGreen(p)
        cRed,cGreen = cGreen,cRed
        setRed(p,cRed)
        setGreen(p,cGreen)

def esercizioFacileA_alternativa(pict):
    #@Param pict:Picture
    for y in range(0,getHeight(pict)):
        for x in range(0,getWidth(pict)):
            p = getPixel(pict,x,y)
            cRed = getRed(p)
            cGreen = getGreen(p)
            cRed,cGreen = cGreen,cRed
            setRed(p,cRed)
            setGreen(p,cGreen)

def esercizioFacileB(pict):
    #@Param pict:Picture
    listPixels = getPixels(pict)
    tot = 0.0
    N = len(listPixels)
    for index in range(0,N):
        p = listPixels[index]
        cRed = getRed(p)
        tot = tot + cRed
    media = tot / N
    print "la media aritmetica e': ",media
def esercizioFacileB(pict):
    #@Param pict:Picture
    tot = 0.0
    N = getHeight(pict)*getWidth(pict)
    for x in range(0,getWidth(pict)):
        for y in range(0,getHeight(pict)):
            p = getPixel(pict,x,y)
            cRed = getRed(p)
            tot = tot + cRed
    media = tot / N
    print "la media aritmetica e': ",media
