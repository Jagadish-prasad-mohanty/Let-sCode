def Merge(arr1,arr2,n,m):
    i=0
    j=0
    k=n-1
    while(i<=k and j<m):
        if arr1[i]<arr2[j]:
            i+=1
        else:
            x=arr1[k]
            arr1[k]=arr2[j]
            arr2[j]=x
            j+=1
            k-=1
    arr1.sort()
    arr2.sort()

    print(arr1,arr2)

arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
n=4
m=5

Merge(arr1,arr2,n,m)