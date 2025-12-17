def custom_count(L, value):
    # @param L: list
    # @param value: Any type (string, number, list, tuple, etc.)
    # @return list
    count = 0
    for i in range(0, len(L)):
        if L[i]==value:
            count += 1
    return count
    
L = [1,2,3,4,"pippo",3,"paperino"]
print L
print custom_count(L, 3)