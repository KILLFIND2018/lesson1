def get_matrix(n,m,value):
    matrix  = []
    #для кол-ва строк матрицы, n повторов
    for i in range(n):
        matrix.append([])

        #for для кол - ва столбцов матрицы, m повторов и пополняю список.
        for j in range(m):
            matrix[i].append(value)

    return matrix
result1 = get_matrix(2,2,10)

print(result1)


