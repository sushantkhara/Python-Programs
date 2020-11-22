char = input("Input a letter of the alphabet: ")

if char in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." %char)
elif char == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." %char)

