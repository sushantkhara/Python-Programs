a =[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print("Printing Sorted Element List...")
for i in a:
    print(i)
