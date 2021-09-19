def LCS(a,b,n):

    dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=0
    print(dp)
    maxm=0
    res=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dp[i][j]>maxm:
                # print(maxm,dp[i][j])
                maxm=dp[i][j]
                res=j
    print(maxm,res)
    return b[res-maxm:res]
    

def LPS(arr):
    # n=len(a)
    # if n==0:
    #     return -1
    # if n==1:
    #     return a
    # if n==2:
    #     if a[0]==a[-1]:
    #         return a
    #     else:
    #         return a[0]
    # return LCS(a,a[::-1],n)
    n=len(arr)
    if n==1:
        return arr
    start=0
    maxm=1
    a=0
    b=1
    while b<n:
        i=a
        j=b
        while i>=0 and j<n:
            if arr[i]==arr[j]:
                print("[]",i,j)
                i-=1
                j+=1
            else:
                break
            # print(i,j,arr[i],arr[j])
            if maxm<(j-i-1):
                maxm=j-i-1
                start=i+1
                if maxm==n:
                    return arr[start:start+maxm]
            print("maxm",start,maxm)
        if maxm<(j-i-1):
                    maxm=j-i-1
                    start=i+1
        if maxm==n:
            return arr[start:start+maxm]
        a+=1
        b+=1
        # maxm=j-i
        # start=i
    a=0
    b=2
    while b<n:
        i=a
        j=b
        while i>=0 and j<n:
            if arr[i]==arr[j]:
                print("[]",i,j)
                i-=1
                j+=1
            else:
                break
            # print(i,j,arr[i],arr[j])
            if maxm<(j-i-1):
                maxm=j-i-1
                start=i+1
                if maxm==n:
                    return arr[start:start+maxm]
            print("maxm",start,maxm)
        if maxm<(j-i-1):
                    maxm=j-i-1
                    start=i+1
        if maxm==n:
            return arr[start:start+maxm]
        a+=1
        b+=1
    return arr[start:start+maxm]

a="aaaabcbaa"
# a="rfkqyuquqfjkxy"
#    yxkjfququyqkfr
print(LPS(a))
# abadba
# abdaba
# [[0, 0, 0, 0, 0, 0, 0], 
# [0, 1, 0, 0, 0, 0, 1], 
# [0, 0, 2, 0, 0, 1, 0], 
# [0, 0, 0, 0, 1, 0, 0], 
# [0, 0, 0, 1, 0, 0, 0], 
# [0, 0, 1, 0, 0, 1, 0], 
# [0, 1, 0, 0, 0, 0, 2]]