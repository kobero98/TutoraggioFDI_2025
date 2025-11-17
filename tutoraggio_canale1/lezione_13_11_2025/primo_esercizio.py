def invertiRossoBlu(pict):
# @Param pict:Picture
    width = getWidth(pict)
    height = getHeight(pict)
    for x in range(0,width):
        for y in range(0,height):
            p = getPixel(pict,x,y)
            r = getRed(p)
            b = getBlue(p)
            if r < b:
                setRed(p,b)
                setBlue(p,r)

def invertiRossoBlueAlternativa(pict):
# @Param pict:Picture
    listPixels = getPixels(pict)
    for index in range(0,len(listPixels)):
        p = listPixels[index]
        r = getRed(p)
        b = getBlue(p)
        if r < b:
            setRed(p,b)
            setBlue(p,r)


