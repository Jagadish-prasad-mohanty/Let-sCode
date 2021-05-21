def findZeroes(arr, n, m) :
    # code here
    c=m
    start=0
    ml=0
    l=0
    i=0
    ml=0
    while i<n:
        if arr[i]==1:
            l+=1
            
        else:
            if c>0:
                c-=1
                l+=1
                if c+1==m:
                    start=i+1
            else:
                i=start
                c=m
                if ml<l:
                    ml=l
                l=0
        i+=1
        if ml<l:
            ml=l
    return ml

print(findZeroes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],11,2))