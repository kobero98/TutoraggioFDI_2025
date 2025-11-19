def lineDetect(orig, threshold):
    # @param orig: Picture
    # @param threshold: int differenza di luminosita' per tracciare il bordo
    # @return Picture
    # makeBW e' l'immagine che verra' modificata tracciando i bordi
    makeBW = duplicatePicture(orig)
    for x in range(0, getWidth(orig)-1):
        for y in range(0, getHeight(orig)-1):
            here=getPixel(makeBW, x, y)
            down=getPixel(orig, x, y+1)
            right=getPixel(orig, x+1, y)
            hereLum=(getRed(here)+getGreen(here)+getBlue(here))/3
            downLum=(getRed(down)+getGreen(down)+getBlue(down))/3
            rightLum=(getRed(right)+getGreen(right)+getBlue(right))/3
            if (abs(hereLum-downLum)>threshold) and (abs(hereLum-rightLum)>threshold):
                setColor(here , black)
            if (abs(hereLum-downLum)<=threshold) or (abs(hereLum-rightLum)<=threshold):
                setColor(here , white)
    return makeBW

pict = makePicture(pickAFile())
out = lineDetect(pict, 2)
show(out)