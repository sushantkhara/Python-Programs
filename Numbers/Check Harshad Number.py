""" If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.

For example:

The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).

Some Harshad numbers are 8, 54, 120, etc. """

num = int(input("Enter a number:"))
rem = sum = 0

# Make a copy of num and store it in variable n
n = num

# Calculates sum of digits
while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

# Checks whether the number is divisible by the sum of digits
if n % sum == 0:
    print(str(n) + " is a harshad number")
else:
    print(str(n) + " is not a harshad number")