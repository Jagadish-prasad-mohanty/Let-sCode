def romanToDecimal(S): 
    dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    l=len(S)
    s=dic[S[l-1]]
    for i in range(l-2,-1,-1):
        if dic[S[i]]<dic[S[i+1]]:
            s-=dic[S[i]]
        else:
            s+=dic[S[i]]

    return s

print(romanToDecimal('XLVII'))
