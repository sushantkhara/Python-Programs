arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
copyArr = [None]*len(arr)   # OR copyArr = [0]*len(arr)

for i in range(0, len(arr)):
    copyArr[i] = arr[i]


print("Elements of the original array:")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print()

print("Elements of the new array:")
for i in range(0, len(copyArr)):
    print(copyArr[i], end=" ")

