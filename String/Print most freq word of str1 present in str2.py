# Print most frequent word from S1 that is present in S2
str1 = "hi hello hi aloha"
str2 = "hi code hi algorithm"
freq_words = [word for word in str1.split() if word in str2.split()]
most_freq_words = [max(freq_words, key=freq_words.count)]
print(most_freq_words)
"""for element in list1:
    if element in list2:
        common_count += 1
        if common_count >= 2:
            print(list(set(list1).intersection(list2)))
        else:
            print("Sorry!! There are no such words...")"""





