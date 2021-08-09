def relativeSort(A1,N,A2,M):
    temp=dict()
    for i in A1:
        if i not in temp:
            temp[i]=0
        temp[i]+=1
    res=[]
    for i in A2:
        if i in temp:
            res.extend([i]*temp[i])
            # for j in range(temp[i]):
            #     res.append(i)
            temp[i]=0
    x=[]
    for i in temp:
        if temp[i]!=0:
            x.extend([i]*temp[i])
    x.sort()
    return res+x

# x=relativeSort([1,3,1,2,5,9],6,[3,2,1],3)
x=relativeSort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8],11,[2, 1, 8, 3],4)
print(x)