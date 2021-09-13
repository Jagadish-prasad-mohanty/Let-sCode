def rMatrix(arr,n,m):
    i=0
    j=m-1
    maxm=0
    while(j>=0 and i<n):
        if arr[i][j]==1:
            j-=1
            maxm=m-1-j
        else:
            i+=1

        
    return maxm

print(rMatrix([[0, 1, 1, 1],
           [0, 0, 1, 1],
           [0, 0, 1, 1],
           [0, 0, 0, 0]],4,4))
