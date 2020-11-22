# Reverse of a string or characters reverse in string
s = " my name is khan!"
# Using slicing
# print(" Reverse of the string:", s[::-1])
rev = " "
# Using for loop to reverse words too
for i in s:
    rev = i + rev
print(rev)


# using reversed method
# print(" Reverse of the string:", rev.join(reversed(s)))

# keep words as it is , remove spaces(leading and trailing), reverse the sentence preserve words


def rev_string(s):
    return " ".join(reversed(s.split()))

# OR


def rev_string2(s2):
    return " ".join(s2.split()[::-1])
