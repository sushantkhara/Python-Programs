# getMissingNo takes list as argument
def get_missing_no(array):
    n = len(array)
    total = (n + 1) * (n + 2) / 2
    arr_sum = sum(array)
    return total - arr_sum


# Driver program to test above function
A = [1, 2, 4, 5, 6]
miss = get_missing_no(A)
print(miss)

# Second way :


def finder(arr1, arr2):
    num = 0
    for n in arr1:
        num += n
    for n in arr2:
        num -= n
    return num
    pass


finder([2, 2, 5, 6, 4, 3, 1, 9, 7], [7, 5, 6, 3, 4, 9])

# Third way :


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


finder([2, 2, 5, 6, 4, 3, 1, 9, 7], [7, 5, 6, 3, 4, 9])

# Using Collections
import collections


def finder(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


finder([5, 5, 7, 7], [5, 7, 7])
