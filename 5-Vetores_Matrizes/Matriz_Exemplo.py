N = 3
M = 3
mat = [[0]*M for i in range(N)]
i = 0
while i < N:
    j = 0
    while j < M:
        mat[i][j] = int(input(f"Valor ({i} {j}): "))
        j += 1
    i += 1
print(mat)
i = 0
while i < N:
    j = 0
    while j < M:
        print (mat[i][j])
        j += 1
    i += 1
