from random import randint

val1 = input("Enter lower limit to generate random numbers: ")
val2 = input("Enter upper limit to generate random numbers: ")
val3 = input("How many random numbers to print ? ")
lower = int(val1)
upper = int(val2)
amount = int(val3)
print()

for i in range(0, amount):
    print(randint(lower, upper), end=" ")
