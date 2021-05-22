def factorial(arr,n):
    maxm=10**5
    maxmArr=[0]*(maxm+1)
    mod=10**9+7

    maxmArr[0]=1
    for i in range(1,maxm+1):
        maxmArr[i]=((maxmArr[i-1]%mod)*i)%mod
    
    res=[0]*n
    for i in range(n):
        res[i]=maxmArr[arr[i]]
    return res

print(factorial([0,1,2,3,4],5))

