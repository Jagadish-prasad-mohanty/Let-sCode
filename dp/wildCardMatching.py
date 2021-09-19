def WCM(pattern,strg):
    n=len(pattern)
    m=len(strg)
    dp=[[False for i in range(n+1)] for j in range(m+1)]

    dp[0][0]=True
    # print(dp)
    for j in range(1,n+1):
        if pattern[j-1]=='*':
            dp[0][j]=dp[0][j-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[j-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif pattern[j-1]=='?' or strg[i-1]==pattern[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=False

    print(dp)
print(WCM("ab*b?","abaaaba"))

# [[True, False, False, False, False, False], 
# [False, True, False, False, False, False], 
# [False, False, True, True, False, False], 
# [False, False, False, True, False, False], 
# [False, False, False, True, False, False], 
# [False, False, False, True, False, False], 
# [False, False, False, True, True, False], 
#  [False, False, False, True, False, True]]