def finite_taylor(d):
    n = len(d)
    mat = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        mat[i][i] = d[i]
    for i in range(1,n):
        for j in range(0,n-i):
            mat[i+j][j] = mat[i+j-1][j] + mat[i+j][j+1]
    return mat
