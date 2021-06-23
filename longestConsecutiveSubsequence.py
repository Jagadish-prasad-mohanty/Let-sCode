# def findLongestConseqSubseq(arr, N):
#     maxArr=max(arr)
#     temp=[0]*(maxArr+1)
#     for i in arr:
#         temp[i]=1

#     count=0
#     maxC=0
#     for i in range(maxArr+1):
#         if temp[i]==1:
#             count+=1
#         else:
#             if maxC<count:
#                 maxC=count
#             count=0

#     return maxC

def findLongestConseqSubseq(arr, N):
    s=set(arr)
    ans=0
    for i in range(N):
        if arr[i]-1 not in s:
            j=arr[i]
            while j in s:
                j+=1
            
            ans=max(ans,j-arr[i])

    return ans


print(findLongestConseqSubseq([2,6,1,9,4,5,3],7))


