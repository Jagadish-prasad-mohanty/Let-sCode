def isSubsetSum ( N, arr, sum):
        # code here 
        dp=[[-1 for i in range(sum+1)] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if (i==0):
                    dp[i][j]=False
                if j==0:
                    dp[i][j]=True
        for i in range(1,N+1):
            for j in range(1,sum+1):
                print(i,j)
                if arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    
        return dp[N][sum]

print(isSubsetSum(6,[3, 34, 4, 12, 5, 2],9))