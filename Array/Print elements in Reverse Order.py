# Initialize array
arr = [1, 2, 3, 4, 5]
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print()
print("Array in reverse order: ")
# Loop through the array in reverse order
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")
