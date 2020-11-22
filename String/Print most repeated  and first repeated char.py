s = input("Enter a String:")

"""
def first_repeated(str):
    h = {}  # Create empty hash
# Traverse each characters in string  in lower case order
    for ch in str:
# If character is already present  in hash, return char
        if ch in h:
            return ch;
# Add ch to hash
        else:
            h[ch] = 0

    return '\0'


print(first_repeated(s))"""

# Most repeated character in string:
"""# Find most repeated using max() function. You could use a list of tuples of the form (letter, number_of_occurrences)
# Populate the list iterating over the string or using list comprehensions, then sort it with the key lambda x: -x[1]:

user_string = input("Please enter a string: ").lower()
print(max(((letter, user_string.count(letter)) for letter in user_string), key=lambda x: [1])[0]) """

# without using max() function through set
# count = [(i, s.count(i)) for i in set(s)]

# Another way

max_repeat = 0
for i in s:
    if s.count(i) > max_repeat:
        max_repeat = s.count(i)
print(i)
print(max_repeat)
# Using collections
# import collections
# str = "sample string"
# print "Max occurring character is " +
#        collections.Counter(str).most_common(1)[0][0]



