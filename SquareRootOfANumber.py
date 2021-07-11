def floorSqrt(x):
    i=0
    j=x//2
    while i<=j:
        mid=(i+j)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            if (mid+1)*(mid+1)>x:
                return mid
            elif (mid+1)*(mid+1)==x:
                return mid+1
            i=mid+1

        else:
            if (mid-1)*(mid-1)<=x:
                return mid-1
            j=mid-1

print(floorSqrt(2))