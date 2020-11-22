str1 = "hi hello hi cao hi aloha"
str2 = "hello code run algorithm"

print("Before swap:\n")
print("First string:", str1)
print("Second string:", str2)


"""temp = str1      
str1 = str2
str2 = temp"""
str1 = str1 + str2
str2 = str1.replace(str2, "")
str1 = str1.replace(str2, "")
""" # Without Using Built-in function 
# Extract str2 from updated str1  
str2 = str1[0 : (len(str1) - len(str2))] 
#Extract str1 from updated str1  
str1 = str1[len(str2):] 
"""
print("After Swap:\n")
print("First string:", str1)
print("Second string:", str2)
