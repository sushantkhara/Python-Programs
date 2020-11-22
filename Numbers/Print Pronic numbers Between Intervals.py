""" The pronic number is a product of two consecutive integers of the form: n(n+1).

For example:

6 = 2(2+1)= n(n+1),
72 =8(8+1) = n(n+1)

Some pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56 etc. """


# isPronicNumber() will determine whether a given number is a pronic number or not
def isPronicNumber(num):
    flag = False

    for j in range(1, num + 1):
        # Checks for pronic number by multiplying consecutive numbers
        if (j * (j + 1)) == num:
            flag = True
            break
    return flag


# Displays pronic numbers between 1 and 100
print("Pronic numbers between 1 and 100 are: ")
for i in range(1, 101):
    if isPronicNumber(i):
        print(i, end=" ")
