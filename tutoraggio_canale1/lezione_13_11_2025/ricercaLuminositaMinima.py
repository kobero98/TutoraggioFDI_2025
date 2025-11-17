

def lumen(pix):
#   @Param pix:Pixel
#   @Return integer
    return getBlue(pix)+getRed(pix)+getGreen(pix)
def minLumPicture(pict):
#   @Param pict:Picture
#   @Return integer
    listPixels = getPixels(pict)
    if len(listPixels)<1:
        return
    m = lumen(listPixels[0])
    for i in range(1,len(listPixels)):
        actualLumen = lumen(listPixels[i])
        if actualLumen < m:
            m = actualLumen
    return m
def minLumPicture(pict):
#   @Param pict:Picture
#   @Return integer
    m = lumen(getPixel(pict,0,0))
    for x in range(0,getWidth(pict)):
        for y in range(0,getHeight(pict)):
            actualLumen = lumen(getPixel(pict,x,y))
            if actualLumen < m:
                m = actualLumen
    return m
