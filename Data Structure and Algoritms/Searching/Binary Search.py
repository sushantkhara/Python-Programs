# Using Recursion


def binary_search(arr, beg, end, item):
    if end >= beg:
        mid = int((beg + end) / 2)
        if arr[mid] == item:
            return mid + 1
        elif arr[mid] < item:
            return binary_search(arr, mid + 1, end, item)
        else:
            return binary_search(arr, beg, mid - 1, item)
    return -1


arr = [16, 19, 20, 23, 45, 56, 78, 90, 96, 100]
item = int(input("Enter the item you want to search?\n"))
location = -1
location = binary_search(arr, 0, 9, item)
if location != -1:
    print("Item found at location %d" %location)
else:
    print("Item not found")

# Using Iterative Method

"""def binary_search(alist, key):
    # Search key in arr[start... end - 1].
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end) // 2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1"""


""" arr = input('Enter the sorted list of numbers: ')
arr = arr.split()
arr = [int(x) for x in arr]
item = int(input('The number to search for: '))

index = binary_search(arr, item)
if index < 0:
    print('{} was not found.'.format(item))
else:
    print('{} was found at index {}.'.format(item, index)) """


