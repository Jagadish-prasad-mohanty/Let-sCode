
def CountWays(str):
    		# Code here
    n=len(str)
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    1213
    # 1 1 2 
    for i in range(2,n+1):
        if str[i-1]>'0':
            dp[i]=dp[i-1]

        if str[i-2]=='1' or str[i-2]=='2' and str[i-1]<'7':
            dp[i+=dp[i-2]

    return dp[n]
print(CountWays('1213'))