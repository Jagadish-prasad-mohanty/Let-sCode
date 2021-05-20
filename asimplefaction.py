def fractionToDecimal(numerator, denominator):
    left=numerator//denominator
    if numerator%denominator==0:
        return left
    rem=numerator%denominator
    rm=dict()
    res=""
    while (rem!=0) and (rem not in rm):
        rm[rem]=len(res)

        rem*=10
        res_part=rem//denominator
        res+=str(res_part)
        rem%=denominator

    if rem==0:
        return numerator/denominator
    else:
        return ".".join([str(left),str(res[:rm[rem]])+"("+res[rm[rem]:]+")"])

print(fractionToDecimal(11,18))
