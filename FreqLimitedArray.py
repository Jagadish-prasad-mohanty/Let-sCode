def frequencyCount(arr, N, P):
    for i in range(N):
        arr[i]-=1
    arr.sort()
    ind=N
    for i in range(N):
        if arr[i]>=N:
            arr[i]=0
            if ind==N:
                ind=i

    for i in range(ind):
        arr[arr[i]%N]=arr[arr[i]%N]+N


arr=[2,6,4,8,5]
N=5
frequencyCount(arr,N,5)
for i in arr:
    print(i//N)