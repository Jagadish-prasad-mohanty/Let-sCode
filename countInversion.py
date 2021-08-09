def mergeSort(arr,n):
    tempArr=[0]*n
    return _mergeSort(arr,tempArr,0,n-1)

def _mergeSort(arr,tempArr,l,r):
    iCount=0
    if l<r:
        mid=(l+r)//2
        iCount+=_mergeSort(arr,tempArr,l,mid)
        iCount+=_mergeSort(arr,tempArr,mid+1,r)
        iCount+=merge(arr,tempArr,l,mid,r)
        
    return iCount

def merge(arr,tempArr,l,mid,r):
    i=k=l
    j=mid+1
    invCount=0

    while(i<=mid and j<=r):
        if arr[i]<=arr[j]:
            tempArr[k]=arr[i]
            i+=1
            k+=1
        else:
            invCount+=(mid-i+1)
            tempArr[k]=arr[j]
            j+=1
            k+=1
    while j<=r:
        tempArr[k]=arr[j]
        j+=1
        k+=1
    while i<=mid:
        tempArr[k]=arr[i]
        i+=1
        k+=1
    

    for i in range(l,r+1):
        arr[i]=tempArr[i]
    return invCount


print(mergeSort([2, 4, 1, 3, 5],5))
    

