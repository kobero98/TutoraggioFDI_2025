def lum(pix):
    # @param pix: Pixel
    # @return int
    return (getRed(pix)+getGreen(pix)+getBlue(pix))

def isLumInPict(pict, l):
    # @param pict: Picture
    # @param l: int
    # @return bool
    allPix = getPixels(pict)
    for j in range(0, len(allPix)):
        l1 = lum(allPix[j])
        if l == l1:
            return True
    return False

def isEquiLum(pict1, pict2):
    # @param pict1: Picture
    # @param pict2: Picture
    # @return bool
    allPix = getPixels(pict1)
    for i in range(0, len(allPix)):
            l = lum(allPix[i])
            if isLumInPict(pict2, l)==False:
                return False
    return True


pict1 = makeEmptyPicture(10,10, blue)
pict2 = makeEmptyPicture(10,10,pink)
print isEquiLum(pict1,pict2)