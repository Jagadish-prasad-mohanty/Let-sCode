def kadene(arr,n):
    maxm=0
    summ=0
    for i in range(n):
        summ+=arr[i]
        if summ<=0:
            summ=0
            
        if summ>maxm:
            maxm=summ
            
    return maxm

def circularSubarraySum(arr,n):
    if max(arr)<0:
        return max(arr)
    maxKadene=kadene(arr,n)
    print(maxKadene)
    maxSum=0
    for i in range(n):
        maxSum+=arr[i]
        arr[i]=-arr[i]

    print(maxSum)
    maxSum+=kadene(arr,n)
    print(maxSum)

    if maxSum>maxKadene:
        return maxSum
    return maxKadene




print(circularSubarraySum([8,-8,9,-9,10,-11,12],7))