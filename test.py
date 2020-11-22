def fib_iter(n):
    if n <= 2:
        return 1
    n1 = n2 = 1
    n3 = 0
    for i in n(3, n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
    return n3


num = int(input("Enter number of sequence:"))
fib_iter(num)

