str1 = input("Please Enter Your Own String : ")

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        print("Vowels in this String are:\n", i)

    elif i >= 'a' and i<= 'z' or i >= 'A' and i<= 'Z' :
        print("Consonants in this String are:\n", i)
