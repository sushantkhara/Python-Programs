"""
A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly. If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number.

Let's understand by an example:

Number = 32
3^2+ 2^2 = 13
1^2 + 3^2 = 10
1^2 + 0^2 = 1

In this example, we split 32 to get the sum of squares of its digits which forms another number (13), we replace 32 by 13 to continue this cycle until result 1. We found 32 a happy number.

If the above cycle for any number results in 1 then that number will be a Happy number otherwise that will be an unhappy number resulting 4, 16, 37, 58, 89, 145, 42, 20,.....

Some Happy numbers are 7, 28, 100, 320, etc. """


# isHappyNumber() will determine whether a number is happy or not
def HappyNumber(num):
    rem = sum = 0

    # Calculates the sum of squares of digits
    while num > 0:
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


num = int(input("Enter a number:"))
result = num

while result != 1 and result != 4:
    result = HappyNumber(result)

# Happy number always ends with 1
if result == 1:
    print(str(num) + " is a happy number")
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif result == 4:
    print(str(num) + " is not a happy number")