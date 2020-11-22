import array
arr1 = array.array('i', [0, 1, 2, 4, 5, 6, 7, 8, 9])
arr2 = array.array('i', [40, 50, 16, 18, 90])

arr3 = array.array('i')
arr3 = arr1 + arr2
print("The new created array is:", arr3)

