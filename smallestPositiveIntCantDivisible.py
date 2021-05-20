def smallestpositive(array, n): 
    array.sort()
    summ=1
    for i in array:
        if i<=summ:
            summ+=i
        else:
            break
    return summ
print(smallestpositive([1 ,1, 3 ,5 ,8 ,21],6))