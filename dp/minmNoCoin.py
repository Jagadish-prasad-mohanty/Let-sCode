import math
def minmCoin(coins,M,V):
    dp=[[math.inf for i in range(V+1)] for j in range(M+1)]
    for i in range(M+1):
        for j in range(V+1):
            if (j==0 ):
                dp[i][j]=0
            
    for j in range(1,V+1):
        if j%coins[0]==0:
            dp[1][j]=j//coins[0]
    # print(dp)
    for i in range(2,M+1):
        for j in range(1,V+1):
            if coins[i-1]<=j:
                dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)

minmCoin([3,7,4],3,49)

# [[0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
# [0, inf, inf, 1, inf, inf, 2, inf, inf, 3, inf, inf, 4, inf, inf, 5, inf, inf, 6, inf, inf, 7, inf, inf, 8, inf, inf, 9, inf, inf, 10, inf, inf, 11, inf, inf, 12, inf, inf, 13, inf, inf, 14, inf, inf, 15, inf, inf, 16, inf], 
# [0, inf, inf, 1, inf, inf, 2, 1, inf, 3, 2, inf, 4, 3, inf, 5, 4, inf, 6, 5, inf, 7, 6, inf, 8, 7, inf, 9, 8, inf, 10, 9, inf, 11, 10, inf, 12, 11, inf, 13, 12, inf, 14, 13, inf, 15, 14, inf, 16, 15], 
# [0, inf, inf, 1, 1, inf, 2, 1, inf, 3, 2, 2, 4, 3, 3, 5, 4, 4, 6, 5, 5, 7, 6, 6, 8, 7, 7, 9, 8, 8, 10, 9, 9, 11, 10, 10, 12, 11, 11, 13, 12, 12, 14, 13, 13, 15, 14, 14, 16, 15]]

