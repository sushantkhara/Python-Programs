from collections import Counter

"""
def second_frequent(input):
    # Convert given list into dictionary
    # it's output will be like {'ccc':1,'aaa':3,'bbb':2}
    dict = Counter(input)

    # Get the list of all values and sort it in ascending order
    value = sorted(dict.values(), reverse=True)

    # Pick second largest element
    second_large = value[1]

    # Traverse dictionary and print key whose
    # value is equal to second large element
    for (key, val) in dict.items():
        if val == second_large:
            print(key)
            return


# Driver program
if __name__ == "__main__":
    input = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
second_frequent(input)"""

# Using lambda expression

string = "Ravi had been saying that he had been there"


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_x)
    return counts_x[-2]


print(word_count(string))

