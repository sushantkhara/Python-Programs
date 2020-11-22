# define punctuation
punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_"""
# take input from the user
my_str = input("Enter a string: ")
# remove punctuation from the string
no_punctuation = ""


for char in my_str:
    if char not in punctuation:
        no_punctuation += char

# display the un-punctuated string
print(no_punctuation)
