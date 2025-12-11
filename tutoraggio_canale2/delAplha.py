def delAlpha(s):
    # @param s: stringa
    # @return stringa
    str = ""
    i = 0
    while i<len(s):
        if s[i].isdigit():
            str += s[i]
        i += 1
    return str

def delDigit(s):
    # @param s: stringa
    # @return stringa
    str = ""
    i = 0
    while i<len(s):
        if s[i].isalpha():
            str += s[i]
        i += 1
    return str

s = "1234asdf"
print s
s1 = delDigit(s)
s2 = delAlpha(s)
print s, " - ", s1, " - ", s2