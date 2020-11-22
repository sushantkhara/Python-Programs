#  character frequency
s = input("Enter a string:")
# Using loop
"""char, word = 0, 1

for i in S:
    char += 1
    if i == ' ':
        word += 1

print(" There are", char, "of chars  and", word, " words in the string")"""

# char frequency without using count()
"""
all_freq = {}


def char_freq():
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1


char_freq()
print(" The no of chars in the string are:", str(all_freq))"""

# Find word frequency using dict without using count() method

b = {}
for word in s.split():
    b[word] = b.get(word, 0)+1      # Start scanning word and count freq and increment it


for key in sorted(b):               # Sort all keys i.e words and print word freq
    print("{} : {}".format(key, b[key]))
