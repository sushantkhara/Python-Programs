A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
print("There are", len(A), "rows", "and", len(A[0]), "cols")
# calculate no. of rows and cols
row = len(A)
col = len(A[0])
# calculate sum of each row
for i in range(row):
    rowSum = 0
    for j in range(col):
        rowSum += A[i][j]
    print("sum of ", i+1, "row:", rowSum)
# calculate sum of each col
for i in range(col):
    colSum = 0
    for j in range(row):
        colSum += A[j][i]
    print("sum of ", i+1, "col:", colSum)
# calculate sum of diagonal elements
for i in range(row):
    diagonalSum = 0
    for j in range(col):
        if i == j:
            diagonalSum += A[i][j]
    print("sum of diagonals:", diagonalSum)



