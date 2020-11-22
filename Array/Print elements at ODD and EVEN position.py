# Initialize array
arr = [1, 2, 3, 4, 5]

print("Elements of given array present on even position: ")
# Loop through the array by incrementing the value of i by 2

# Here, i will start from 1 as first even positioned element is present at position 1.
for i in range(1, len(arr), 2):
    print(arr[i], end=" ")
print()
print("Elements of given array present on odd position: ")
# Loop through the array by incrementing the value of i by 2

for i in range(0, len(arr), 2):
    print(arr[i], end=" ")
