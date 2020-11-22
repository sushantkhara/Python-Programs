"""
A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. For example, 175 is a Disarium number as follows:

1^1+ 7^2 + 5^3 = 1+ 49 + 125 = 175 """

# calculateLength() will count the digits present in a number
def calculateLength(n):
    length = 0
    while n != 0:
        length = length + 1
        n = n // 10
    return length


num = int(input("Enter a number:"))
rem = sum = 0
len = calculateLength(num)

# Makes a copy of the original number num
n = num

# Calculates the sum of digits powered with their respective position
while num > 0:
    rem = num % 10
    sum = sum + int(rem ** len)
    num = num // 10
    len = len - 1

# Checks whether the sum is equal to the number itself
if sum == n:
    print(str(n) + " is a disarium number")
else:
    print(str(n) + "is not a disarium number")