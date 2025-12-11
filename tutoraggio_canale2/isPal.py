def isPal(s):
    # @param s: string
    # @return bool
    i = 0
    while i<(len(s)/2): 
        if s[i] == s[-i-1]:
            i += 1
        else:
            return False
    return True

s = "osso"
s1 = "ossesso"
print s
print s1
print isPal(s), " - ", isPal(s1)