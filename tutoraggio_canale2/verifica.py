def verifica(L):
    # @param L: list
    # @return bool
    if sum(L[::2]) == sum(L[1::2]):
        return True
    return False

L = [1,0,3,4]
print verifica(L)