def stampaPosPari(vettore=[3,5,12,31,43,7,11]):
#@Param vettore:list of integer
    for i in range(0,len(vettore),2):
        print "vettore[",i,"]=",vettore[i]
def stampaPosDisapri(vettore=[3,5,12,31,43,7,11]):
#@Param vettore:list of integer
    for i in range(1,len(vettore),2):
        print "vettore[",i,"]=",vettore[i]
def stampaPos(vettore=[3,5,12,31,43,7,11],dispari=0):
#@Param vettore:list of integer
    for i in range(dispari,len(vettore),2):
        print "vettore[",i,"]=",vettore[i]

