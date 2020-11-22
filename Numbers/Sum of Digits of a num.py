num = int(input("Enter a number:"))
sum = r = 0
while num > 0:
	r = num %10
	sum += r
	num //= 10
print(sum)
