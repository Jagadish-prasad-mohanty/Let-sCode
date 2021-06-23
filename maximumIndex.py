def maxmIndexDiff(arr,n):
    arrL=[0]*n
    arrR=[0]*n
    arrL[0]=arr[0]
    for i in range(1,n):
        arrL[i]=min(arr[i],arrL[i-1])
    arrR[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        arrR[i]=max(arr[i],arrR[i+1])

    i=j=0
    maxDiff=-1
    while(i<n and j<n):
        if arrL[i]<=arrR[j]:
            maxDiff=max(maxDiff,j-i)
            # print(maxDiff)
            j+=1

        else:
            i+=1
    return maxDiff
print(maxmIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1],9))
                 
