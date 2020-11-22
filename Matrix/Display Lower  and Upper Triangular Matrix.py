""" Lower triangular matrix is a square matrix in which all the elements above the principle diagonal will be zero.
To find the lower triangular matrix, a matrix needs to be a square matrix that is, the number of rows and columns in
the matrix need to be equal. Dimensions of a typical square matrix can be represented by n x n."""


# Function to form lower triangular matrix
def lower(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if i < j:
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")

        print(" ")


# Function to form upper triangular matrix
def upper(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if (i > j):
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")

        print(" ")


# Driver Code
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
row = 3
col = 3

print("Lower triangular matrix: ")
lower(matrix, row, col)

print("Upper triangular matrix: ")
upper(matrix, row, col)

