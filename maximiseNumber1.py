# def findZeroes(arr, n, m) :
#     # code here
#     c=m
#     start=0
#     ml=0
#     l=0
#     i=0
#     ml=0
#     while i<n:
#         if arr[i]==1:
#             l+=1
            
#         else:
#             if c>0:
#                 c-=1
#                 l+=1
#                 if c+1==m:
#                     start=i+1
#             else:
#                 i=start
#                 c=m
#                 if ml<l:
#                     ml=l
#                 l=0
#         i+=1
#         if ml<l:
#             ml=l
#     return ml

def findZeroes(arr, n, m):
    # code here
    wl=wr=bestW=countZ=0
    
    while wr<n:
        if countZ<=m:
            if arr[wr]==0 and countZ!=m:
                countZ+=1
                wr+=1
            elif arr[wr]==0 and countZ==m:
                if arr[wl]==0:
                    countZ-=1
                wl+=1
            else:
                wr+=1
                
            
            
        if (wr-wl)>bestW:
            bestW=wr-wl
        print(wr,wl)
    return bestW

print(findZeroes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],11,2))
# [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],11,2