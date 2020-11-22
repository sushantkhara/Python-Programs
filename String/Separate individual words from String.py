string = "characters plays vital role to build a word"
word = string.split()
# Displays individual characters from given string
print("Individual characters from given string:")

# Iterate through the string and display individual character
for i in range(0, len(word)):
    print(word[i], ",", end="  ")
