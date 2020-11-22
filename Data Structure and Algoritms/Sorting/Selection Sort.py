def smallest(a, i):
    small = a[i]
    pos = i
    for j in range(i + 1, len(a)):
        if a[j] < small:
            small = a[j]
            pos = j
    return pos


a = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
for i in range(0, len(a)):
    pos = smallest(a, i)
    temp = a[i]
    a[i] = a[pos]
    a[pos] = temp
print("printing sorted elements...")
for i in a:
    print(i)
