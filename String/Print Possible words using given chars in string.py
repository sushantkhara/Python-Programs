# Function to print words which can be created using given set of characters
from collections import Counter


def possible_words(input, charset):
    # traverse words in list one by one
    for word in input:

        # convert word into dictionary
        dict = Counter(word)

        # now check if all keys of current word are present in given character set
        flag = 1
        for key in dict.keys():
            if key not in charset:
                flag = 0

        # if all keys are present ( flag=1 ), then print the word
        if flag == 1:
            print(word)

# Driver program


if __name__ == "__main__":
    input_chars = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
    charset = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(input_chars, charset)
