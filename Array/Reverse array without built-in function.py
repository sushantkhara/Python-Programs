import array
arr1 = array.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original array is:", arr1)
# reverse = arr1[::-1]    # Using Slicing technique

# print("Reversed array is:", reverse)
print("Reversed array is:", end=" ")
# Using for loop
for i in range(len(arr1)-1, -1, -1):
    print(i, end=" ")

