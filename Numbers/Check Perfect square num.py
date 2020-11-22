import math

n = int(input("Enter a number:"))

i = int(math.sqrt(n))  # square root function returns float so typecasting to int

if n == i*i:
        print("It is a perfect Square")
else:
    print("Not Perfect Square")
