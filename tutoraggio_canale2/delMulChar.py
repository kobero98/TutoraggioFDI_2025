def delMulChar(s):
    # @param s: string
    # @return string
    str = ""
    for i in range(0, len(s)):
        if s[i] == " " or str.find(s[i]) == -1:
            str += s[i]
        else:
            str += "*"
    return str

s = "la mia casa bianca"
print s, "\n", delMulChar(s)

            
        