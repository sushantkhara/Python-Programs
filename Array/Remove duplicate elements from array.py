# This program is to remove duplicate elements from list using set
"""
a =[]
n= int(input("Enter the number of elements in list:"))
for x in range(0, n):
    element = int(input("Enter element" +str(x+1) + ":"))
    a.append(element)
b = list(set(a))

print("Non-duplicate items are:")
print(b)
"""
# Remove duplicates from list preserving order:
list1 = [5, 1, 2, 4, 0, 1, 2, 5, 0]
print(f"list: {list1}")
noDuplicates = list(dict.fromkeys(list1))
print(f"no duplicates: {noDuplicates}")
"""
# Program to remove duplicate elements from array using array

import array

a = array.array('i', [1, 2, 3, 1, 2, 3, 5, 5])
li = []
for i in a:
    if i not in li:
        li.append(i)


print("The new array created is : ", end="")
print(li, end=" ")"""
