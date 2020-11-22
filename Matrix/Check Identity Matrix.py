# Identity Matrix: A matrix is said to be an identity matrix if it is a square matrix in which elements of principle diagonal are ones, and the rest of the elements are zeroes.
# example: [[1, 0, 0], [0,1, 0], [0, 0, 1]]
# python program to print Identity Matrix:
"""n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print() """

# program to check Identity Matrix:

row = int(input("Enter the no. of rows:"))
column = int(input("Enter the no. of columns:"))
matrix =[]
for i in range(row):
    matrix.append([0]*column)
    for j in range(column):
        matrix[i][j] = int(input("Enter the elements:"))

flag = 0
for i in range(row):
    for j in range(column):
        if i == j and matrix[i][j] == 1:
            pass
        elif i !=j and matrix[i][j] == 0:
            pass
        else:
            flag = 1

if flag == 0:
    print(" Its an Identity Matrix!!")
else:
    print("Its not an Identity Matrix!!")