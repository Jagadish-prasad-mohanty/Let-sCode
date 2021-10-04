import sys
def isPalindrome(st,a,b):
    # print(st[a:b+1],st[b:a-1:-1],a,b)
    if a==0:
        if st[a:b+1]!=st[b::-1]:
            return False
    else:
        if st[a:b+1]!=st[b:a-1:-1]:
            return False
    # i=a
    # j=b
    # while(i<j):
    #     if st[i]!=st[j]:
    #         return False
    #     i+=1
    #     j-=1
    return True
def findPar(st,i,j,dp):
    if j-i<=1:
        return 0
    if isPalindrome(st,i,j-1):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    minm=sys.maxsize
    for k in range(i+1,j):
        temp_ans=findPar(st,i,k,dp)+findPar(st,k,j,dp)+1
        
        minm=min(minm,temp_ans)
    dp[i][j]=minm
    return minm
    
def pp(st):
    n=len(st)
    dp=[[-1 for i in range(n+1)] for j in range(n+1)]

    return findPar(st,0,n,dp)
st="aaabba"
print(pp(st))

