# Checks for the largest common prefix
def lcp(s, t):
    n = min(len(s), len(t))
    for i in range(0, n):
        if s[i] != t[i]:
            return s[0:i]
    else:
        return s[0:n]

# Checks for the Shortest common prefix


def srp(s):
    for k in range(1, len(s) + 1):
        l = s.split()
        sub = min(l, key=len)
        repeats = len(s) // len(sub)

        if sub * repeats == s:
            return (sub, repeats)


str1 = "aacbdfbdfaa"
lrs = " "
n = len(str1)
for i in range(0, n):
    for j in range(i + 1, n):
        # Checks for the largest common factors in every substring
        x = lcp(str1[i:n], str1[j:n])
        # If the current prefix is greater than previous one then it takes the current one as longest repeating sequence
        if len(x) > len(lrs):
            lrs = x
print("Longest repeating sequence: " + lrs)
print("Shortest repeating sequence: \n", srp(str1))
