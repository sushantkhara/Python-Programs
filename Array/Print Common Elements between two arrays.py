import array
arr1 = array.array('i', [0, 1, 2, 4, 5, 6, 7, 8, 9])
arr2 = array.array('i', [0, 2, 40, 50, 16, 7, 18, 90])

print("The common elements are:")
for i in arr1:
    for j in arr2:
        if i in arr1 and i in arr2:
            arr1.remove(i)  # and arr2.remove(i) to remove
            print(i, end=" ")





