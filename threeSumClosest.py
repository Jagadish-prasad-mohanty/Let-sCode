import sys
def sumClosest(arr,n,t):
    if n==3:
        return sum(arr)
    arr.sort()
    res=sys.maxsize
    for i in range(n-2):
        j=i+1
        z=n-1
        while j<z:
            check=arr[i]+arr[j]+arr[z]
            if abs(t-check)<abs(t-res):
                res=check
            if check>t:
                z-=1
            else:
                j+=1
    return res


print(sumClosest([-7,9,8,3,1,1],6,2))