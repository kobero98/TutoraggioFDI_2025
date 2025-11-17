def esercizio3B(pict,K):
# @Param pict:Picture
# @Param K:integer
    upperBound = min(K,getWidth(pict))
    height = getHeight(pict)
    for x in range(0,upperBound):
        for y in range(0,height):
            p = getPixel(pict,x,y)
            b = getBlue(p)
            r = getRed(p)
            setRed(p,b)
            setBlue(p,r)

def tracciaRettaVerticale(pict,x0,x1,y):
# @Param pict:Picture
# @Param x0:integer
# @Param x1:integer
# @Param y:integer
    lBound = min(y0,y1)
    uBound = max(y0,y1)
    for x in range(lBound,uBound):
        p = getPixel(pict,x,y)
        setColor(p,black)

def esercizio3C(pict,x0,y0,x1,y1):
# @Param pict:Picture
# @Param x0:integer
# @Param x1:integer
# @Param y0:integer
# @Param y1:integer
    if x0==x1:
        tracciaRettaVerticale(pict,y0,y1,x0)
        return
    step = 1
    if x0>x1:
        step = -step
    m = (y1-y0) / float(x1-x0)
    q = (x0*y1 - x1*y0)/float(x0-x1)
    for x in range(x0,x1+1,step):
        y = m*x + q
        y = int(y)
        p = getPixel(pict,x,y)
        setColor(p,black)
