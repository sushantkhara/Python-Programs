""" Two matrices are said to be equal if and only if they satisfy the following conditions:
1. Both the matrices should have the same number of rows and columns.
2. Both the matrices should have the same corresponding elements."""

# This function returns 1
# if A[][] and B[][] are identical
# otherwise returns 0
N = 4
def areSame(A, B):
    for i in range(N):
        for j in range(N):
            if (A[i][j] != B[i][j]):
                return 0
    return 1


# driver code
A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

B = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

if (areSame(A, B) == 1):
    print("Matrices are identical")
else:
    print("Matrices are not identical")