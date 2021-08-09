def diagonalSort(matrix,n,m):
    lower_trangle=[[] for i in range(n)]
    upper_trangle=[[] for i in range(m)]
    # major=[]
    for i in range(n):
        for j in range(m):
            if i>j:
                lower_trangle[i-j].append(matrix[i][j])
            elif i<j:
                upper_trangle[j-i].append(matrix[i][j])
            # else:
            #     major.append(matrix[i][j])

    for i in range(n):
        lower_trangle[i].sort(reverse=True)
    for j in range(m):
        upper_trangle[j].sort()
    print(lower_trangle)
    print(upper_trangle)
    for i in range(n):
        for j in range(m):
            d=abs(i-j)
            if i>j:
                matrix[i][j]=lower_trangle[d].pop()
            elif i<j:
                matrix[i][j]=upper_trangle[d].pop()

    return matrix
print(diagonalSort([[3, 6 ,3 ,8 ,2],
                    [4 ,1 ,9 ,5 ,9],
                    [5, 7 ,2 ,4 ,8],
                    [8, 3, 1 ,7, 6]],4,5))



        
