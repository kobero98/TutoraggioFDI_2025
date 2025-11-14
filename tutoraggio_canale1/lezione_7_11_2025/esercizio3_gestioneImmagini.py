def esercizio3A(pic,K):
# @Param pic: Picture
# @Param K:integer
    width = getWidth(pic)
    height = getHeight(pic)
    upperBound = min(K-1,width)
    tot = 0.0
    n = upperBound * height
    for x in range(0,upperBound):
        for y in range(0,height):
            p = getPixel(pic,x,y)
            cRed = getRed(p)
            tot = tot + cRed
    media = tot/n
    print "la media delle componenti Red dei pixel e': ",media

#esercizio 3B
def privacy2(pict,xmin,xmax,ymin,ymax):
# @Param pict:Picture
# @Param xmin:int
# @Param xmax:int
# @Param ymin:int
# @Param ymax:int
    height = getHeight(pict)
    width = getWidth(pict)
    xL = min(xmin,xmax)
    yL = min(ymin,ymax)
    xU = max(xmin,xmax)
    yU = max(xmin,xmax)

    lBoundX = max(0,xL)
    uBoundX = min(width,xU)
    lBoundY = max(0,yL)
    uBoundY = min(height,yU)

    for x in range(lBoundX,uBoundX):
        for y in range(lBoundY,uBoundY):
            p = getPixel(pict,x,y)
            setColor(p,black)
