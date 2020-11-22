# The solution is to loop through the string for each character and search for the same in the rest of the string.


def find_repeat_first(s):
    p = -1
    for i in range(len(s)):

        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                p = i
                break
        if p != -1:
            break
    return p


# Driver code
if __name__ == "__main__":

    string = "heyhihello"
    pos = find_repeat_first(string)
    if pos == -1:
        print("Not found")
    else:
        print(string[pos])
