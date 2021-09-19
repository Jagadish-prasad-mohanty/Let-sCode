def findMax(arr,dp,s,e):
    if s>e:
        return 0

    if dp[s][e]==-1:
        return dp[s][e]
    a=arr[s]-findMax(arr,dp,s+1,e)
    b=arr[e]-findMax(arr,dp,s,e-1)

    dp[s][e]=max(a,b)

    return dp[s][e]
def maxScore(arr,n):
    dp=[[-1 for i in range(n)] for j in range(n)]
    return findMax(arr,dp,0,n-1)>=0

print(maxScore([2,6,3],3))