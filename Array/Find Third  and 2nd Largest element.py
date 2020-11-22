arr = [25, 11, 7, 75, 56]
arr2 = [1, 2, 5, 6, 3, 2]


# function to get Third Largest
def get_third_largest(arr, total):
    for i in range(total):
        for j in range(i+1, total):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr[total-3]

# function to get Second Largest


def get_second_largest(arr, total):
    for i in range(total):
        for j in range(i+1, total):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr[total-2]


print("The third largest element in arr is:", get_third_largest(arr, 5))
print("The third largest element in arr2 is:", get_third_largest(arr2, 6))
print("The Second largest element in arr is:", get_second_largest(arr, 5))
print("The Second largest element in arr2 is:", get_second_largest(arr2, 6))
