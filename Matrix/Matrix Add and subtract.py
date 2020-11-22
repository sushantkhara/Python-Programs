'''X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

Result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        Result[i][j] = X[i][j] + Y[i][j]  # for subtraction:  X[i][j] - Y[i][j]
for r in Result:
    print(r) '''

# To take matrix input from user:
# The beauty of this approach is that if the user enters [[1,2],[3,4]] at the prompt which yields the string '[[1,2],[3,4]]') then literal_eval converts this string to the list [[1,2],[3,4]].
import ast
X = ast.literal_eval(input("Enter the first 2x2 matrix as a list of lists: "))
Y = ast.literal_eval(input("Enter the second 2x2 matrix: "))
result = [[0, 0], [0, 0]]
# iterate through rows
for i in range(len(X)):
  # iterate through columns
  for j in range(len(X[0])):
    result[i][j] = X[i][j] + Y[i][j]    # for subtraction:  X[i][j] - Y[i][j]
for r in result:
    print(r)

"""
# To take input and print for nxn matrix
rows = int(input("Enter number of rows in the matrix: "))
columns = int(input("Enter number of columns in the matrix: "))
matrix = []
print("Enter the %s x %s matrix: "% (rows, columns))
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))
    for j in range(columns):
        matrix.append(list(map(int, input().rstrip().split())))
        print(matrix)
"""

