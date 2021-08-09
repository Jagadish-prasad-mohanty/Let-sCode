# def findMissing(arr1,arr2,n,m):
#     i=j=0
#     arr1.sort()
#     arr2.sort()
#     res=[]
#     while(i<n and j<m):
#         if arr1[i]==arr2[j]:
#             i+=1
#             j+=1
#         elif arr1[i]<arr2[j]:
#             res.append(arr1[i])
#             i+=1
#         else:
#             j+=1

#     return res+arr1[i:]
def findMissing(arr1,arr2,n,m):
    res=dict()
    ans=[]
    for i in range(n):
        res[arr1[i]]=1
    for i in range(m):
        if arr2[i] in res:
            res[arr2[i]]+=1

    for i in res:
        if res[i]==1:
            ans.append(i)

    
    return ans
        



    return res+arr1[i:]


print(findMissing([1, 2, 3, 4, 5, 10],[2, 3, 1, 0, 5],6,5))