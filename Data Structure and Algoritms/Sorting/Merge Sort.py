# Recursive Algorithm
def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def merge_sort(list):
    if len(list) < 2:
        return list

    middle = len(list) / 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    return merge(left, right)


seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq)
print("\n")
print("Sorted array is")
print(merge_sort(seq))

# Iterative Algorithm
# array to be sorted
""" Array = [99, 21, 19, 22, 28, 11, 14, 18]


# function for merging two sub-arrays
def merge(left, right, Array):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            Array[k] = left[i]
            i = i + 1
        else:
            Array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        Array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        Array[k] = right[j]
        j = j + 1
        k = k + 1


# function for dividing and calling merge function
def merge_sort(Array):
    n = len(Array)
    if n < 2:
        return

    mid = n / 2
    left = []
    right = []

    for i in range(mid):
        number = Array[i]
        left.append(number)

    for i in range(mid, n):
        number = Array[i]
        right.append(number)

    merge_sort(left)
    merge_sort(right)
    merge(left, right, Array)


# calling merge_sort
merge_sort(Array)
for i in Array:
    print(i)        """
