def LCS(arr,n):
    s=set()
    for i in range(n):
        s.add(arr[i])
    res=0
    for i in range(n):
        if arr[i]-1 not in s:

            j=arr[i]
            while j in s:
                j+=1

            res=max(res,j-arr[i])


    return res

print(LCS([2,6,1,9,4,5,3],7))