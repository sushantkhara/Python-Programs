arr = [10, 2, 3, 4, 23, 5, 21]
item = int(input("Enter the item which you want to search:"))
flag = 1
for i in range(0, len(arr)):
    if arr[i] == item:
        flag = i
        break
    else:
        flag = 0
if flag != 0:
    print("Item found at location %d" %flag)
else:
    print("Item not found")
