# def productExceptSelf(nums, n):
#     if n==1:
#         return [1]

#     prod=[1 for i in range(n)]

#     temp=1
#     for i in range(n):
#         prod[i]*=temp
#         temp*=nums[i]
#     temp=1
#     for i in range(n-1,-1,-1):
#         prod[i]*=temp
#         temp*=nums[i]

#     return prod
def productExceptSelf(nums, n):
    if n==1:
        return [1]
    mul=1
    flag=0
    for i in range(n):
        if nums[i]!=0:
            mul*=nums[i]
        else:
            flag+=1
    
    p=[]
    if flag==1:
        for i in range(n):
            if nums[i]==0:
                p.append(mul)
            else:
                p.append(0)
    elif flag>1:
        for i in range(n):
            p.append(0)
    else:
        for i in range(n):
            p.append(mul//nums[i])
    return p

print(productExceptSelf([1,2,3,4],4))
    