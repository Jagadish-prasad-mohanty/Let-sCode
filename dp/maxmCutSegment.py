import math
def maxmCut(N,x,y,z):
    n=3
    arr=[x,y,z]
    dp=[[-1 for i in range(N+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(N+1):
            if (j==0 ):
                dp[i][j]=0
            
    for j in range(1,N+1):
        if j%arr[0]==0:
            dp[1][j]=j//arr[0]
    # print(dp)
    for i in range(2,n+1):
        for j in range(1,N+1):
            if arr[i-1]<=j:
                if dp[i][j-arr[i-1]]!=-1:
                    dp[i][j]=max(dp[i][j-arr[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)
    return dp[n][N]

print(maxmCut(100,23,15,50))
