# First Repeated word
"""from collections import Counter
string = "Ravi had been saying that he had been there"


def first_repeat(input):
    # first split given string separated by space into words
    words = input.split(' ')
    # now convert list of words into dictionary
    word_dict = Counter(words)
    # traverse list of words and check which first word  has frequency > 1
    for key in words:
        if word_dict[key] > 1:
            print(key)
            return


first_repeat(string)"""

# find most repeated
from collections import Counter

string = "hi hello bye fellow how are you doing hi hi"
# split() returns list of all the words in the string
split_it = string.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common()

print(most_occur)
