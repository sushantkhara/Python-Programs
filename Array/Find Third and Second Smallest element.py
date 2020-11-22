arr = [25, 11, 7, 75, 56]
arr2 = [1, 2, 5, 6, 3, 2]


# function to get Third Smallest
def get_third_smallest(arr, total):
    for i in range(total):
        for j in range(i+1, total):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr[2]


# function to get Second Smallest
def get_second_smallest(arr, total):
    for i in range(total):
        for j in range(i+1, total):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr[1]


print("The third smallest element in arr is:", get_third_smallest(arr, 5))
print("The third smallest element in arr2 is:", get_third_smallest(arr2, 6))
print("The Second smallest element in arr is:", get_second_smallest(arr, 5))
print("The Second smallest element in arr2 is:", get_second_smallest(arr2, 6))
