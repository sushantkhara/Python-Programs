"""s = " Python is an elegant language "
print("The substrings are:", end=" ")
# print substrings together in a string
print(str.split(s))
"""
s = " Python"


def get_all_substrings(input_string):
        length = len(input_string)
        return [input_string[i:j+1] for i in range(length) for j in range(i, length)]


print(get_all_substrings(s))
# Another way of using function to print substrings

"""
def get_all_substrings(string):
        for i in range(len(string)):
                print(string[i:])
                get_all_substrings((string[i:i-1]))


get_all_substrings(s)"""

