# Transpose Matrix:If you change the rows of a matrix with the column of the same matrix, it is known as transpose of a matrix. It is denoted as X'. For example: The element at ith row and jth column in X will be
# placed at jth row' and ith column in X'

"""X = [[1, 2],
     [4, 5],
     [7, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)    """

# To take input from the user:
row = int(input("Enter the no. of rows:"))
column = int(input("Enter the no. of columns:"))
matrix =[]
for i in range(row):
    matrix.append([0]*column)
    for j in range(column):
        matrix[i][j] = int(input("Enter the elements:"))

result = [[0 for x in range(row)] for y in range(column)]
def transpose(matrix, result):
    for i in range(column):
        for j in range(row):
            result[i][j] = matrix[j][i]


transpose(matrix, result)

print("Result matrix is")
for i in range(column):
    for j in range(row):
        print(result[i][j], " ", end='')
    print()
