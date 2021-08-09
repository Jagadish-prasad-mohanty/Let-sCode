# def minimumPlatform(n,arr,dep):
#     stamp=[dep[0]]
#     flag=0
#     for i in range(1,n):
#         for j in range(len(stamp)):
#             if arr[i]>stamp[j]:
#                 flag=1
#                 stamp[j]=dep[i]
#                 break
#         if (flag==0):
#             stamp.append(dep[i])
#         else:
#             flag=0

#     return len(stamp) 
def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    n=len(arr)
    plat=1
    res=1
    i=1
    j=0
    while(i<n and j <n):
        if (arr[i]<=dep[j]):
            plat+=1
            i+=1
        elif arr[i]>dep[j]:
            plat-=1
            j+=1

        if res<plat:
            res=plat

    return res

print(minimumPlatform(6,[900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))



# Input: n = 6 
# arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
# dep[] = {0910, 1200, 1120, 1130, 1900, 2000}