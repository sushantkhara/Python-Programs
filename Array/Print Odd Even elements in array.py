arr = [1, 2, 3, 4, 5, 6]
print("Odd no.s in array are:")

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        print(arr[i], end=" ")

print()

print("Even no.s in array are:")

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")

