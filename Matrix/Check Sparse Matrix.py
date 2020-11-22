# A matrix is said to be Sparse Matrix if most of the elements of that matrix are 0. It implies that it contains very less non-zero elements.
# To check whether the given matrix is the sparse matrix or not, we first count the number of zero elements present in the matrix. Then calculate the size of the matrix.
# For the matrix to be sparse, count of zero elements present in an array must be greater than size/2.
"""
# Initialize matrix a
a = [[4, 0, 0], [0, 5, 0], [0, 0, 6]]
#Calculates numbern of rows and columns present in given matrix
rows = len(a)
cols = len(a[0])
#Calculates the size of array
size = rows * cols
# Count all zero element present in matrix
count = 0
for i in range (rows):
    for j in range(cols):
        if a[i][j] == 0:
                count += 1

if count > (size / 2):
    print("Given matrix is a sparse matrix")
else:
    print("Given matrix is not a sparse matrix") """

# To take Input from user:
rows = int(input("Enter the no. of rows:"))
cols = int(input("Enter the no. of columns:"))
matrix =[]
#Calculates the size of array
size = rows * cols

for i in range(rows):
    matrix.append([0]*cols)
    for j in range(cols):
        matrix[i][j] = int(input("Enter the elements:"))

# Count all zero element present in matrix
count = 0
for i in range (rows):
    for j in range(cols):
        if matrix[i][j] == 0:
                count += 1

if count > (size / 2):
    print("Given matrix is a sparse matrix")
else:
    print("Given matrix is not a sparse matrix")
