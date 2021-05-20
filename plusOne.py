def increment(arr, N):
    # code here 
    arr[:]=arr[::-1]
    carry=0
    if arr[0]==9:
        arr[0]=0
        carry=1
    else:
        arr[0]+=1
        return arr[::-1]
    for i in range(1,N):
        if arr[i]==9:
            arr[i]=0
            carry=1
        else:
            arr[i]+=1
            return arr[::-1]
            
    if carry!=0:
        arr.append(carry)
        return arr[::-1]


print(increment([1,2,4],3))