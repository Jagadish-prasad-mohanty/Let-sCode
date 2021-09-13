def hasArray(arr, n, x):
    s=set()
    for i in arr:
        if i not in s:
            s.add(x-i)
        else:
            print(s)
            return 'YES'
    return 'NO'

print(hasArray([1,4,56,5,10,8],6,16))