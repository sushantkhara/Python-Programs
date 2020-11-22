import array

""" # To take input from user
a = array.array('i')
n = int(input("Enter number of elements:"))
for i in range(1, n+1):
    b = int(input("Enter element:"))
    a.append(b)
"""
arr1 = array.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

n = int(input("Enter an element to find its position:"))
print(" The position of", n, " is ", arr1.index(n))
