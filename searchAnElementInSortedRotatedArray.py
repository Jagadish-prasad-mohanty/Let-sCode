def Search(arr,n,k):
    i=0
    j=n-1

    pivot=findPivot(arr,i,j)


    if arr[pivot]==k:
        return pivot
    if arr[0]<=k:
        return binarySearch(arr,i,pivot-1,k)
    return binarySearch(arr,pivot+1,j,k)
    


def findPivot(arr,l,h):
    if l==h:
        return l
    
    mid=(l+h)//2

    if arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid]<arr[mid-1]:
        return mid-1

    if arr[l]<=arr[mid]:
        return findPivot(arr,mid+1,h)
    return findPivot(arr,l,mid-1)

def binarySearch(arr,l,h,k):
    if l>h:
        return -1
    mid=(l+h)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]<k:
        return binarySearch(arr,mid+1,h,k)
    return binarySearch(arr,l,mid-1,k)


print(Search([5 ,6,7,8,9,10,1,2,3],9,10))