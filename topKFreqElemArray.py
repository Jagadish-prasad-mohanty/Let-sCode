def topK(nums, key):
    		#Code here
    d=dict()
    for i in nums:
        if i not in d:
            d[i]=0
        d[i]+=1
    a=[]
    for i in d:
        a.append([i,d[i]])

    # print(a)
    a=sorted(a,key=lambda x:x[0],reverse=True)
    # print(a)
    a=sorted(a,key=lambda x:x[1],reverse=True)
    # print(a)
    res=[]
    for i in range(key):
        res.append(a[i][0])
    return res





print(topK([6,1,1,2,2,2,3],2))