dec = int(input("Enter a decimal number: "))

print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

""" To convert decimal to binary:
n = int(input("Enter a number:"))
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2, end='')

convertToBinary(n)

To convert Binary to decimal:
binary = input("Enter number in Binary Format: ")
decimal = int(binary, 2)
print(binary,"in Decimal =",decimal)
"""