rev = rem = 0
num = int(input("Enter a number:"))
temp = num
while num > 0:
	rem = num % 10
	rev = rev*10 + rem
	num //= 10
print(rev)
if temp == rev:
	print("Its a Palindrome number!!")
else:
	print("Not a Palindrome number!!")
