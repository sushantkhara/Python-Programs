from collections import Counter

string = "hi hi hi hello bye fellow how are you doing?"
# split() returns list of all the words in the string
split_it = string.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered input values and their respective counts.
most_occur = Counter.most_common(1)
print("Max occurring word is:", most_occur)
print("Min occurring word is:", min(split_it, key=split_it.count))




