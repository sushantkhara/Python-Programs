# isPalindrome() checks whether a string is palindrome or not
def is_palindrome(a):
    flag = True
    # Iterate the string forward and backward and compare one character at a time until middle of the string is reached
    for i in range(0, len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            flag = False
            break
    return flag


string = "Wow you are great mom kanak"
words = []
word = ""
count = 0
# Converts the given string into lowercase
string = string.lower()
# Add extra space after string to get the last word in the given string
string = string + " "

for i in range(0, len(string)):
    # Split the string into words
    if string[i] != ' ':
        word = word + string[i]
    else:
        # Add word to array words
        words.append(word)
        # Make word an empty string
        word = ""

    # Determine the smallest and biggest palindromes in a given string
for i in range(0, len(words)):
    if is_palindrome(words[i]):
        count = count + 1
        # When first palindromic word is found
        if count == 1:
            # Initialize smallPalin and bigPalin with first palindromic word
            small = big = words[i]

            # Compare small and big palindrome with each palindromic words
        else:
            # If length of small is greater than next palindromic word  Store that word in small palindrome
            if len(small) > len(words[i]):
                small = words[i]

                # If length of big is less than next palindromic word Store that word in big Palindrome
            if len(big) < len(words[i]):
                big = words[i]

if count == 0:
    print("No palindrome is present in the given string")
else:
    print("Smallest palindromic word: " + small)
    print("Biggest palindromic word: " + big)
