def custom_reverse(L):
    # @param L: list
    # @return list
    L1 = []
    size = len(L)
    for i in range(0, size):
        L1.append(L[-i-1])
    return L1

L = [1,2,3,4]
print L
print custom_reverse(L)
        