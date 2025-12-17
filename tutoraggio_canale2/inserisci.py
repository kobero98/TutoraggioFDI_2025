def inserisci(L, n1, n2):
    # @param L: list
    # @param n1, n2: Any type (string, number, list, tuple, etc.)
    # @return list
    for i in range(0, len(L)):
        if L[i]==n1:
            L = L[:i+1]+[n2]+L[i+1:]
    return L
    
L = [1,2,3,4,"pippo",3,"paperino"]
print L
print inserisci(L, "pippo", 3)