def find_height(arr,n,k):
    if n==1:
        if arr[0]>k:
            return arr[0]-k
    arr.sort()
    summ=0
    count=1

    for i in range(n-2,-1,-1):
        if k-summ<(arr[i+1]-arr[i])*count:
            if k-summ==((k-summ)//count)*count:
                return arr[i+1]-(k-summ)//count
            else:
                return -1

        summ+=count*(arr[i+1]-arr[i])
        count+=1

        if k==summ:
            return arr[i]
        
        if k<summ:
            break
    return -1

print(find_height([81, 13, 36, 65 ,38 ,69],6,48))