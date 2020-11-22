"""nterms = int(input("How many terms you want? "))
# first two terms
n1 = 0
n2 = 1
count = 2
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
print(n1, ",", n2, end=', ')
while count < nterms:
    nth = n1 + n2
    print(nth, end=' , ')
    # update values
    n1 = n2
    n2 = nth
    count = count + 1

"""
# Fibonacci Series Using Recursion:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
      return recur_fibo(n-1) + recur_fibo(n-2)
# take input from the user


nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Please enter a positive integer")
else:  
    print("Fibonacci sequence:")
    for i in range(nterms):
       print(recur_fibo(i))