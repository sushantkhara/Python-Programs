"""X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows of X
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)"""

# To take matrix input from user:
# The beauty of this approach is that if the user enters [[1,2],[3,4]] at the prompt which yields the string '[[1,2],[3,4]]') then literal_eval converts this string to the list [[1,2],[3,4]].

import ast
X = ast.literal_eval(input("Enter the first row for 2x2  matrix as a list of lists: "))
Y = ast.literal_eval(input("Enter the second row for  2x2 matrix: "))
result = [[0, 0], [0, 0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        for k in range(len(Y)):
            result[i][j] = result[i][j] + X[i][k] * Y[k][j]  # for division:  X[i][j]/Y[i][j]
for r in result:
        print(r)