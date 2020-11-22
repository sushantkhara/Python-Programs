# Using temp
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
print("Before Swap numbers are:\n")
print(n1)
print(n2)
"""temp = n1
n1 = n2
n2 = temp
print("After Swapping numbers are:\n")
print(n1)
print(n2)"""

# Without Using Temp or third variable
n1 = n1 + n2
n2 = n1 -n2
n1 = n1- n2
print("After Swapping numbers are:\n")
print(n1)
print(n2)
