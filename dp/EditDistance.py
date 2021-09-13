def distance(a,b):
    n=len(a)
    m=len(b)
    if (n==0): return m
    if (m==0): return n
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if (i==0):
                dp[i][j]=j
            if (j==0):
                dp[i][j]=i
    print(dp)
    for i in range(1,n+1):
        for j in range(1,m+1):
            # if (i==0):
            #     dp[i][j]=j
            # if (j==0):
            #     dp[i][j]=i
            if (a[i-1]==b[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    print(dp)
    return dp[n][m]
    
# print(distance('dab','bad'))
print(distance('ecfbefdcfca','badfcbebbf'))
#         g   e  s  k
#  * [[0, 0, 0, 0, 0], 
#  g [0, 1, 1, 1, 1], 
#  e [0, 1, 2, 2, 2], 
#  e [0, 1, 2, 2, 2], 
#  k [0, 1, 2, 2, 3]]
# i=3
# j=3
# res= eek
# esk