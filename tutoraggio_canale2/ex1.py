def lum(pix):
    # @param pix: Pixel
    # @return int
    return (getRed(pix)+getGreen(pix)+getBlue(pix))

def lumLinea(pict, y):
    # @param pict: Picture
    # @param y: int
    # @return bool
    l = lum(getPixel(pict, 0, y))
    for x in range(1, getWidth(pict)):
        l1 = lum(getPixel(pict,x,y))
        if l1 != l:
          return False
    return True

def nLumEqRow(pict):
    # @param pict: Picture
    # @return int
    count = 0
    for y in range(0, getHeight(pict)):
        bool = lumLinea(pict,y)
        if bool == True:
            count = count+1
    return count


pict = makeEmptyPicture(200,200,red)
print nLumEqRow(pict)