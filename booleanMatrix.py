def boolean(matrix):
    r=len(matrix)
    c=len(matrix[0])
    i=j=0
    data=set()
    while i<r:
        flag=j=0
        while j<c:
            if matrix[i][j]==1:
                data.add(j) 
                flag=1
            j+=1
        if flag==1:
            matrix[i]=[1]*c
        i+=1
    for i in range(r):
        for j in range(c):
            if j in data:
                matrix[i][j]=1
    return matrix

print(boolean([[ 1, 0, 0],
              [ 1, 0, 0],
              [ 1, 0, 0],
              [ 0, 0, 0]]))