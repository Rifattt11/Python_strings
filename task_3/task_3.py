import re

text = input("Введите текст: ")

words = re.findall(r'[a-zа-яё]+', text.lower())

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("Топ-5 самых частых слов:")
for word, count in sorted_words[:5]:
    print(word, "-", count)