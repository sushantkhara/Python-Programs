# to check and count the entered chars in a string is space, digit/number, alphabet/letter, special/punctuation char
str1 = input("Enter a string/char:")
# to print the chars directly:
"""print("The alphabets are:\n", ''.join(e for e in str1 if e.isalpha()))
print("The digits/numbers are:\n", ''.join(e for e in str1 if e.isdigit()))
# for checking a alphanumeric string or char: print("The alphanumerics are:\n",'.join(e for e in str1 if e.isalnum())"""
# for punctuation check: punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_"""
# to count and print
"""s_count = special = d_count = alpha_count = 0   # for punctuation count: p_count = 0
for e in str1:
    if e.isspace():
        s_count += 1
    elif e.isalpha():
        alpha_count += 1
    elif e.isdigit():
        d_count += 1
# for punctuation check: else: p_count += 1; print("The total punctuation chars are:", p_count)
else:
    special += 1

print("The spaces are:", s_count)
print("The alphabets are:", alpha_count)
print("The digits/nums are:", d_count)
print("The special characters are:", special)"""
# without using built-in functions:


def char_check(input_char):
    # CHECKING FOR ALPHABET
    if int(ord(input_char)) >= 65 and int(ord(input_char)) <= 122:
        print(" Alphabet ")

        # CHECKING FOR DIGITS
    elif int(ord(input_char)) >= 48 and int(ord(input_char)) <= 57:
        print(" Digit ")

# OTHERWISE SPECIAL CHARACTER OR for punctuation check: else: p_count += 1;
    # print("The total punctuation chars are:", p_count) OR
    # for space count: else: print("The spaces are:", s_count)
    else:
        print(" Special Character ")

    # Driver Code


char_check(str1)
