def esercizioA1(pict,col,xStart,yStart,height,width):
# @Param pict:Picture
# @Param col:Color
# @Param xStart:integer
# @Param yStart:integer
# @Param height:integer
# @Param width:integer

    hPict = getHeight(pict)
    wPict = getWidth(pict)
    xStart = max(0,xStart)
    yStart = max(0,yStart)
    yUpperBound = min(height+yStart,hPict)
    xUpperBound = min(width+xStart,wPict)
    for x in range(xStart,xUpperBound):
        for y in range(yStart,yUpperBound):
            p = getPixel(pict,x,y)
            setColor(p,col)

def esercizioA2(pict,col):
# @Param pict:Picture
# @Param col:Colore
    h = getHeight(pict)
    w = getWidth(pict)
    if h!=w:
        return
    for x in range(0,w):
        p = getPixel(pict,x,x) #prendo il pixel della diagonale
        setColor(p,col)
        p = getPixel(pict,x,w-1-x) #prendo il pixel dell'antidiagonale
        setColor(p,col)
#esercizio 3A
def disegnaGradino(pict,xStart,yStart,width,height,col):
# @Param pict:Picture
# @Param xStart:integer
# @Param yStart:integer
# @Param height:integer
# @Param width:integer
# @Param col:Color
    pictWidth = getWidth(pict)
    pictHeight = getHeight(pict)
    xUpperBound = min(xStart+width,pictWidth)
    if yStart < pictHeight:
        for x in range(xStart,xUpperBound):
            p = getPixel(pict,x,yStart)
            setColor(p,col)
    yUpperBound = min(yStart+height,pictHeight)
    if xUpperBound < pictWidth:
        for y in range(yStart,yUpperBound):
            p = getPixel(pict,xUpperBound,y)
            setColor(p,col)
def disegnoScala(pict,xStart,yStart,width,height,col):
# @Param pict:Picture
# @Param xStart:integer
# @Param yStart:integer
# @Param height:integer
# @Param width:integer
# @Param col:Color
    pictWidth = getWidth(pict)
    pictHeight = getHeight(pict)
    if xStart<0 or xStart>=pictWidth:
        return 
    if yStart<0 or yStart>=pictHeight:
        return
    numGradini = min((pictWidth-xStart)/width,(pictHeight-yStart)/height))+1
    x = xStart
    y = yStart
    for index in range(0,numGradini):
        disegnoGradino(pict,x,y,width,height,col)
        y = y + height
        x = x + width

def disegnoScala_alternativo(pict,xStart,yStart,width,height,col):
# @Param pict:Picture
# @Param xStart:integer
# @Param yStart:integer
# @Param height:integer
# @Param width:integer
# @Param col:Color
    pictWidth = getWidth(pict)
    pictHeight = getHeight(pict)
    xStart = max(xStart,0)
    yStart = max(yStart,0)
    for x in range(xStart,pictWidth):
        y = ((x-xStart)/width)*height + yStart
        if y > pictHeight -1:
            break
        p = getPixe(pict,x,y)
        setColor(p,col)
    for y in range(yStart,pictHeight):
        x = ((y-yStart)/height + 1)*width + xStart
        if x > pictHeight -1:
            break
        p = getPixe(pict,x,y)
        setColor(p,col)

