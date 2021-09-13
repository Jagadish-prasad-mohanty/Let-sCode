def lpa(arr,n):
        k=1
        flag=1
        res=''
        x=[len(i) for i in arr]
        print(x)
        while k<=min(x):
            count=0
            for i in range(1,n):
                # print(arr[0][:k])
                if arr[0][:k] ==arr[i][:k]:
                    count+=1
            print(count)
            print(res)
            if count!=n-1:
                
                break
            else:
                res= arr[0][:k]
                k+=1
        return res

print(lpa(['d','d','d','d'],4))