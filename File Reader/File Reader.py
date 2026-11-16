import string

with open("Test Text.txt") as file:
    content = file.read()
    word_count = {}
    for word in content.split():
        word = word.lower().strip(string.punctuation)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_count_sorted = sorted(word_count.items(),  key=lambda x: x[1], reverse = True)
    for x in range(10):
        print(word_count_sorted[x])