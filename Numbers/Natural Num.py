''' To Print Natural numbers of given numbers
i = 0
n = int(input("Enter the number up to which you want to print the natural numbers?"))
for i in range(0, n):
    print(i, end =' ')'''
# To Print the sum of natural no.s between range
num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate un till zero
    while num > 0:
        sum += num
        num -= 1
    print("The sum is", sum)  
