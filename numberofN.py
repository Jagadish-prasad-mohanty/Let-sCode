def noN(num):
    n=0
    c=0
    while(num):
        n=(num%9)*((10)**c)+n
        num//=9
        c+=1

    return n

print(noN(100))