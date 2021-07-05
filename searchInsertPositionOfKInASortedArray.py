def searchInsertK(arr,n,k):
    if k>max(arr):
        return n
    if k<arr[0]:
        return 0
    i=0
    j=n-1
    mid=(i+j)//2
    while i<j:
        if arr[mid]==k:
            return mid
        if arr[mid]>k:
            j=mid-1
            mid=(i+j)//2
        else:
            i=mid+1
            mid=(i+j)//2

    return mid

print(searchInsertK([-12 ,-11 ,-3 ,5, 6, 15 ,16, 18],8,19))