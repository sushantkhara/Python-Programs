from collections import Counter

data_set = "Welcome to the world of Geeks " \
           "This portal has been created to provide well written well" \
           "thought and well explained solutions for selected questions " \
           "If you like Geeks for Geeks and would like to contribute " \
           "here is your chance You can write article and mail your article " \
           " to contribute at geeksforgeeks org See your article appearing on " \
           "the Geeks for Geeks main page and help thousands of other Geeks. " \
 \
    # split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(4)  # most_common(4) will return four most frequent words and their count.

print(most_occur)
