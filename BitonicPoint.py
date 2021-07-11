def BitonicPoint(arr,n):
    i=0
    j=n-1
    maxm=-1
    x=0
    while(i<=j):
        mid=(i+j)//2
        if arr[mid]>maxm:
            if arr[mid]>arr[mid-1]:
                i=mid+1
                x=mid
            else:
                j=mid-1
                x=mid

        else:
            if mid>x:
                i=x+1
                j=mid-1
            else:
                j=x-1
                i=mid+1
        
    return arr[mid]

print(BitonicPoint([1,15,25,45],4))



        