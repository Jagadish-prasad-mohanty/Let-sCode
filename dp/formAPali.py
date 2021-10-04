def LCS(S,T,n):
    # dp=[[-1 for j in range(n+1)] for i in range(2)]
    dp=[[-1 for j in range(n+1)] for i in range(n+1)]
    i=1
    i=1-i
    k=1
    maxm=0
    while k<=n:
        for j in range(n+1):
            if S[k-1]==T[j-1]:
                # dp[i][j]=1+dp[1-i][j-1]
                dp[k][j]=1+dp[k-1][j-1]
            else:
                dp[k][j]=0
            if maxm<dp[k][j]:
                maxm=dp[k][j]
        i=1-i
        k+=1
    print(dp,maxm)
    return maxm
                
    
    
    
    
def findMinInsertions(S):
    # code here
    n=len(S)
    if n<=1:
        return 0
    if n<=3 and S[0]==S[-1]:
        return 0
    return n-LCS(S,S[::-1],n)

print(findMinInsertions("helppreanadkada"))
