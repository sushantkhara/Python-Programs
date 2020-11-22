str1 = "aaaabbbbcccc"
# Stores the length of the string
length = len(str1)
# n determines the variable that divide the string in 'n' equal parts
n = 3
temp = 0
chars = int(length/n)
# Stores the array of string
equalStr = []
# Check whether a string can be divided into n equal parts
if length % n != 0:
        print("Sorry this string cannot be divided into " + str(n) +" equal parts.")
else:
    for i in range(0, length, chars):
        # Dividing string in n equal part using substring()
        part = str1[i: i+chars]
        equalStr.append(part)
    print("Equal parts of given string are")
    for i in equalStr:
        print(i)
