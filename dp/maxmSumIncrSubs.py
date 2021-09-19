def maxSumIS(arr, n):
    res=arr[:]
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i] and res[i]<res[j]+arr[i]:
                res[i]=arr[i]+res[j]
            print(res)
    print(res)
    print(arr)
    return max(res)

print(maxSumIS([27 ,39 ,22, 35, 3 ,38 ,48, 4 ,19],9))

