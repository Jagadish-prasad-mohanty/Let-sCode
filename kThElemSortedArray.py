def kthElement(  arr1, arr2, n, m, k):
    i=j=count=0
    maxm=-1
    while(i<n and j<m):
        if arr1[i]>=arr2[j]:
            maxm=arr2[j]
            j+=1
        else:
            maxm=arr1[i]
            i+=1
        count+=1
        if count==k:
            break

    return maxm

print(kthElement([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892],5,7,7))
    