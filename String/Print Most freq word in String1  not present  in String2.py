# Print most frequent word from S1 that is not present in S2
str1 = "hi hello hi hello bye bye"
str2 = "hi code hi algorithm"
list1 = list(str1.split(" "))
list2 = list(str2.split(" "))
no_common = 0

for element in range(len(list1)):
    if element not in list2:
        no_common += 1
        if no_common >= 2:
            print(list(set(list1).difference(list2)))
    else:
        print("Sorry!! There are no such words...")





