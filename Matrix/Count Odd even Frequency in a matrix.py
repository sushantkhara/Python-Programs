A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
# calculate no. of rows and cols
row = len(A)
col = len(A[0])
countOdd = countEven = 0
# calculate frequency of Odd and Even numbers
for i in range(row):
    for j in range(col):
        if A[i][j] % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
print("There are:", countEven, "Even numbers")
print("There are:", countOdd, "Odd numbers")
