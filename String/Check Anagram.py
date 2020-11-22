# An anagram of a string is another string that contains same characters, only the order of characters can be different.
# For example, “abcd” and “dabc” are anagram of each other. another example- 'LISTEN' and 'SILENT'


def is_anagram(str1, str2):
    # Remove spaces and lowercase letters
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()

    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)


print(is_anagram('anagram', 'nagaram'))
print(is_anagram('cat', 'rat'))

'''# Sorting the string to compare without using built in sorted() method


def is_anagram(str1, str2):
    # Remove spaces and lowercase letters
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()

# Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

# Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}

# Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

# Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

# Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

# Otherwise they're anagrams
    return True'''
