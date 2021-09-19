def MLC(arr,n):
    arr.sort(key=lambda x:x[1])
    print(arr)
    check=[]
    check.append(arr[0][1])
    res=[1]
    for i in range(1,n):
        ans=0
        for j in check:
            if ans<j and j<arr[i][0]:
                ans=j
        if arr[i][0]>ans:
            ind=check.index(ans)
            check[ind]=arr[i][1]
            res[ind]+=1
        else:
            check.append(arr[i][1])
            res.append(1)

    print(res)
    print(check)
    return max(res)

print(MLC( [[5 , 24 ], [39 ,60] , [15, 28 ], [27 ,40 ], [50, 90]],5))
print(MLC( [[5,10 ], [1,11]],2))


        