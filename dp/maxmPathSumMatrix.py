def maxSum(arr,n):
    dp=[[0 for i in range(n+2)] for j in range(n+2)]
    for j in range(1,n+1):
        dp[1][j]=arr[0][j-1]
    print(dp)
    for i in range(2,n+1):
        for j in range(1,n+1):
            dp[i][j]=max(arr[i-1][j-1]+dp[i-1][j-1],arr[i-1][j-1]+dp[i-1][j],arr[i-1][j-1]+dp[i-1][j+1])

    print(dp)
    return max(dp[n])

print(maxSum([[5,6,3,2],[7,1,8,5],[1,1,3,4],[2,1,9,5]],4))

