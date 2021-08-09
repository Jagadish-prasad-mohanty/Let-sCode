def countLessThan(arr,n,val):
    arr.sort()
    count=0
    j=k=0
    for i in range(n):
        k=n-1
        j=i+1
        while j<=k:
            x=arr[k]+arr[j]+arr[i]
            if x>val:
                k-=1
            else:
                count+=(k-j)
                j+=1
    return count

def countTriplate(arr,n,l,r):
    res=0
    res=countLessThan(arr,n,r)-countLessThan(arr,n,l-1)
    return res

print(countTriplate([9 ,4 ,6, 1, 2 ,3 ,8],7,3,14))   
