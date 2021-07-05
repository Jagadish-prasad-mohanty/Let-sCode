def findFirst(arr,l,h,x):
    if l>h:
        return -1
    mid=(l+h)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return findFirst(arr,l,mid-1,x)  
    return findFirst(arr,mid+1,h,x)
        
def indexes(arr, x):
    n=len(arr)
    ind=findFirst(arr,0,n-1,x)
    if ind==-1:
        return [-1,-1]
    l=u=ind
    for i in range(ind+1,n):
        if arr[i]==x:
            u=i
        else:
            break
    for i in range(ind-1,-1,-1):
        if arr[i]==x:
            l=i
        else:
            break
        
    return [l,u]

print(indexes([1,2,5,5,5,5,5,12,45,67],5))