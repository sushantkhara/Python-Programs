from collections import Counter


def remove_duplicates(input):
    # split input string separated by space
    input = input.split(" ")

    # joins two adjacent elements in iterable way
    for i in range(0, len(input)):
        input[i] = "".join(input[i])

        # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    unique_word = Counter(input)

    # joins two adjacent elements in iterable way
    s = " ".join(unique_word.keys())
    print(s)


# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remove_duplicates(input)
