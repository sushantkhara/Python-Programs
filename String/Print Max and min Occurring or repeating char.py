str1 = input("Enter a string:")
max_repeat = min_repeat = 0
"""for i in str1:
    if str1.count(i) > max_repeat:
        max_repeat = str1.count(i)
print(i)
print(max_repeat)"""

for j in str1:
    if str1.count(j) < min_repeat:
        min_repeat = str1.count(j)
print(j)
print(min_repeat)
