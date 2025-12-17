def exSum(A):
    # @param A: Picture
    # @return bool
    pxlsL = getPixels(A)
    for i in range(0, len(pxlsL)-1):
        for j in range(i+1, len(pxlsL)):
            if not sum(pxlsL[i], pxlsL[j]):
                return False
    return True

def sum(p1, p2):
     # @param p1: Pixel
     # @param p2: Pixel
     # @return bool
     return getRed(p1) == getGreen(p2)+getBlue(p2)