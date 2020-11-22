s1 = input("Enter a String:")
max_repeat = 0
print("Second Max occurring character is: \n")
for i in s1:
    if s1.count(i) > max_repeat:
        max_repeat = s1.count(i)
        second_max = max_repeat - 1

print(second_max)
s2 = ''.join(sorted(s1))

print(s2[1])
