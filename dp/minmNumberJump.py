# def minmJump(arr,n):
#     i=n-2
#     reach=n-1
#     j=i
#     count=0
#     while i>=0:
#         if i+arr[i]>=reach:
#             j=i
#         if i==0 and reach !=0:
#             count+=1
#             reach=j
#             i=j
#         i-=1
#     if count==0 or reach !=0:
#         return -1
#     return count
# def minmJump(arr,n):
#     ch=n-1
#     if arr[0]==0 or (arr[0]==1 and arr[1]==0):
#     	    return -1
#     count=0
#     for i in range(n-2,-1,-1):
#         if arr[i]+i>=n-1:
#             pass
#         else:
#             ch=i+1
#             count+=1
        # return count
    
# def minmJump(arr,n):
#     if arr[0]==0:
# 	        return -1
#     res=[n]*n
#     res[0]=0
#     for i in range(1,n):
#         for j in range(i):
#             if j+arr[j]>=i and arr[j]!=n:
#                 arr[i]=min(arr[i],arr[j]+1)
#                 break
                
#             # print(res)
    
#     return res[n-1]

def minmJump(arr,n):
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    maxrange=steps=arr[0]
    jump=1
    for i in range(1,n):
        if i==n-1:
            return jump
        maxrange=max(maxrange,i+arr[i])

        steps-=1
        if steps==0:
            jump+=1
            if i>=maxrange:
                return -1
            steps=maxrange-i
    


n = 11 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minmJump(arr,n))