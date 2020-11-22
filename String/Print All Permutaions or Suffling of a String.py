# To print all permutations with duplicates allowed


def to_string(list):
    return ''.join(list)
# Function to print permutations of string. It takes three parameters: 1. String 2. Starting index of the string
# 3. Ending index of the string.


def permute(p, q, r):
    if q == r:
        print(to_string(a))
    else:
        for i in range(q, r + 1):
            a[q], a[i] = a[i], a[q]
            permute(a, q + 1, r)
            a[q], a[i] = a[i], a[q]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
