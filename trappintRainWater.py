# def rainWaterStore(arr,n): 
#     left=[0]*n
#     right=[0]*n
#     maxm=arr[0]
#     for i in range(n):
#         if arr[i]>=maxm:
#             left[i]=arr[i]
#             maxm=arr[i]
#         else:
#             left[i]=maxm
#     maxm=arr[n-1]
#     for i in range(n-1,-1,-1):
#         if arr[i]>=maxm:
#             right[i]=arr[i]
#             maxm=arr[i]
#         else:
#             right[i]=maxm

#     # print(left)
#     # print(right)
#     summ=0
#     for i in range(n):
#         summ+=min(left[i],right[i])-arr[i]

#     return summ
def rainWaterStore(arr,n): 
    right=[0]*n
    
    maxm=arr[n-1]
    for i in range(n-1,-1,-1):
        if arr[i]>=maxm:
            right[i]=arr[i]
            maxm=arr[i]
        else:
            right[i]=maxm

    summ=0
    maxm=arr[0]
    for i in range(n):
        if arr[i]>maxm:
            maxm=arr[i]
        summ+=min(maxm,right[i])-arr[i]

    return summ

    


        

        
print(rainWaterStore([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],12))