a =[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
for k in range(1, len(a)):
    temp = a[k]
    j = k-1
    while j>=0 and temp <=a[j]:
        a[j+1]=a[j]
        j = j-1  
    a[j+1] = temp
print("printing sorted elements...")
for i in a:
    print(i)
