def LIS(n,a):
    if n==1:
        return 1
    
    if n==2:
        if a[0]<a[1]:
            return 2
        return 1

    res=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if a[j]<a[i] and res[i]<res[j]+1:
                res[i]=res[j]+1

    return max(res)

print(LIS(16,[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))
