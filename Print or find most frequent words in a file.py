from string import punctuation
N = 10
words = {}
words_gen = (word.strip(punctuation).lower() for line in open("test.txt")

for word in line.split())
for word in words_gen:
    words[word] = words.get(word, 0) + 1
top_words = sorted(words.items(), key=lambda count, word: (-count, word))[:N]
for word, frequency in top_words:
    print("%s: %d" % (word, frequency))
